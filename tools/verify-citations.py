#!/usr/bin/env python3
"""Mechanical citation verifier for this repository.

Why this exists: language models fabricate references. A DOI, PMID or NCT
number that looks plausible and is even internally self-consistent (right
journal, right year, right author) can still refer to nothing, or refer to
the wrong paper entirely while a different, real identifier for it sits one
sentence over. This programme has already shipped one document that had two
guessed PMIDs corrected only because a human happened to check (see the
verification notes at the bottom of evidence/01-nociceptive-coding.md). A
citation that "looks right" is not evidence; a citation that RESOLVES, live,
against the registry that issued it, is.

This script therefore never infers, guesses or pattern-matches its way to a
verdict. For every identifier it finds in the markdown it makes a real network
call to the authority for that identifier type (Crossref/DataCite for DOIs,
NCBI E-utilities for PMIDs and PMCIDs, arXiv's own API, ClinicalTrials.gov for
NCT numbers) and reports RESOLVED or NOT RESOLVED. The one piece of inference
it performs is a cross-check: when a DOI and a PMID are cited side by side, it
compares their resolved titles, because a real DOI paired with a real but
unrelated PMID is the single most common fabrication pattern and no
per-identifier check catches it.

It is deliberately standard-library only (no pip dependencies) so it runs
unmodified on a bare CI runner and on the author's machine, and it is
deliberately conservative about what counts as a build failure: a registry
having a bad minute (timeouts, 429s, 5xx) is reported as UNREACHABLE and does
not fail the build, because a red CI run for a transient network hiccup
trains authors to ignore red CI runs. A registry cleanly saying "no such
record" always fails the build.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

DEFAULT_CACHE_NAME = ".citation-cache.json"
DEFAULT_TIMEOUT = 15.0
DEFAULT_JOBS = 4
CACHE_FAILURE_TTL_SECONDS = 7 * 24 * 3600
RETRY_DELAYS = (1.0, 2.0, 4.0)  # seconds, applied between retry attempts

# host -> max requests/second. Authoritative regardless of --jobs.
RATE_LIMITS: Dict[str, float] = {
    "api.crossref.org": 5.0,
    "api.datacite.org": 5.0,
    "eutils.ncbi.nlm.nih.gov": 3.0,  # overridden to 10.0 if NCBI_API_KEY is set
    "export.arxiv.org": 1.0 / 3.0,  # one request per three seconds
    "clinicaltrials.gov": 5.0,
}

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
PMID_RE = re.compile(r"PMID[:\s]+(\d{1,8})", re.IGNORECASE)
PMCID_RE = re.compile(r"PMC\d{6,9}")
ARXIV_NEW_RE = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5}(?:v\d+)?)", re.IGNORECASE)
ARXIV_OLD_RE = re.compile(r"arXiv:\s*([a-z-]+(?:\.[A-Z]{2})?/\d{7})", re.IGNORECASE)
NCT_RE = re.compile(r"NCT\d{8}")
ISBN_RE = re.compile(r"ISBN[:\s]*([0-9Xx-]{10,17})", re.IGNORECASE)

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

UNVERIFIED_MARKER = "[UNVERIFIED]"

CONTEXT_WINDOW = 80  # characters either side of a match, for the snippet
PAIR_PROXIMITY = 150  # max character distance for a DOI/PMID cross-check pair
MISMATCH_THRESHOLD = 0.6  # Jaccard word-overlap ratio below which we flag


# --------------------------------------------------------------------------
# Small data types
# --------------------------------------------------------------------------


@dataclass
class Identifier:
    """One citation-like identifier found in one document."""

    idx: int
    id_type: str  # doi | pmid | pmcid | arxiv | nct | isbn
    normalised: str  # value used for cache key / API call
    display: str  # human-readable form for the report
    file: str
    line: int
    col: int
    context: str
    expected_unverified: bool


@dataclass
class ResolveResult:
    ok: bool
    unreachable: bool = False
    registry: Optional[str] = None
    title: Optional[str] = None
    source: Optional[str] = None
    author: Optional[str] = None
    year: Optional[str] = None
    message: str = ""


@dataclass
class Finding:
    """One reportable line: an identifier plus its verdict."""

    identifier: Identifier
    status: str  # ok | FAIL | warn | skip | MISMATCH
    info: str
    detail: Optional[str] = None  # extra context line, e.g. for FAIL


class NetworkError(Exception):
    """Raised after retries are exhausted; maps to UNREACHABLE, not a FAIL."""


# --------------------------------------------------------------------------
# Rate limiting
# --------------------------------------------------------------------------


class RateLimiter:
    """Per-host limiter enforcing a minimum interval between requests.

    Spacing requests by 1/rate seconds guarantees the advertised
    requests-per-second ceiling is never exceeded, which is what the
    registries actually ask for; it is intentionally simpler than a bucket
    that allows bursts, because arXiv in particular is strict.
    """

    def __init__(self, rate_per_second: float) -> None:
        self.min_interval = 1.0 / rate_per_second
        self._lock = threading.Lock()
        self._last = 0.0

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            due = self._last + self.min_interval
            if due > now:
                time.sleep(due - now)
                now = time.monotonic()
            self._last = now


def build_limiters(ncbi_api_key: Optional[str]) -> Dict[str, RateLimiter]:
    limits = dict(RATE_LIMITS)
    if ncbi_api_key:
        limits["eutils.ncbi.nlm.nih.gov"] = 10.0
    return {host: RateLimiter(rate) for host, rate in limits.items()}


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------


def http_get(
    url: str,
    headers: Dict[str, str],
    limiter: RateLimiter,
    timeout: float,
) -> Tuple[int, bytes]:
    """GET with per-host pacing and retry-with-backoff on 429/5xx/network errors.

    Any other status (200, 404, ...) is returned as-is for the caller to
    interpret; only persistent 429/5xx or connection failures raise
    NetworkError, which callers turn into UNREACHABLE (not a build failure).
    """
    last_error: Optional[BaseException] = None
    for attempt in range(len(RETRY_DELAYS) + 1):
        limiter.wait()
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.getcode(), resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code == 429 or 500 <= exc.code < 600:
                last_error = exc
                if attempt < len(RETRY_DELAYS):
                    delay = RETRY_DELAYS[attempt]
                    retry_after = exc.headers.get("Retry-After") if exc.headers else None
                    if retry_after and retry_after.strip().isdigit():
                        delay = float(retry_after)
                    time.sleep(delay)
                    continue
                raise NetworkError(f"HTTP {exc.code} after retries") from exc
            # A clean non-retryable HTTP status (e.g. 404) is meaningful data.
            return exc.code, exc.read()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt < len(RETRY_DELAYS):
                time.sleep(RETRY_DELAYS[attempt])
                continue
            raise NetworkError(str(exc)) from exc
    raise NetworkError(str(last_error) if last_error else "exhausted retries")


def make_headers(mailto: str) -> Dict[str, str]:
    return {
        "User-Agent": (
            f"pain-as-information-citation-verifier/1.0 (mailto:{mailto})"
        )
    }


# --------------------------------------------------------------------------
# Cache
# --------------------------------------------------------------------------


class Cache:
    """JSON-backed cache. Successes never expire; failures expire after 7 days.

    The cache object is passed explicitly wherever it is needed; it is the
    one piece of shared mutable state this tool has, and it owns its own lock
    so it is safe to read/write from the resolver thread pool.
    """

    def __init__(self, path: Optional[Path], enabled: bool) -> None:
        self.path = path
        self.enabled = enabled
        self._lock = threading.Lock()
        self.data: Dict[str, dict] = {}
        if enabled and path is not None and path.exists():
            try:
                self.data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                self.data = {}

    def get(self, key: str) -> Optional[dict]:
        if not self.enabled:
            return None
        with self._lock:
            entry = self.data.get(key)
        if not entry:
            return None
        if entry.get("ok"):
            return entry
        age = time.time() - float(entry.get("ts", 0))
        if age < CACHE_FAILURE_TTL_SECONDS:
            return entry
        return None

    def put(self, key: str, entry: dict) -> None:
        if not self.enabled:
            return
        entry = dict(entry)
        entry["ts"] = time.time()
        with self._lock:
            self.data[key] = entry

    def save(self) -> None:
        if not self.enabled or self.path is None:
            return
        try:
            self.path.write_text(
                json.dumps(self.data, indent=2, sort_keys=True), encoding="utf-8"
            )
        except OSError:
            pass


def result_to_cache_entry(result: ResolveResult) -> dict:
    return {
        "ok": result.ok,
        "registry": result.registry,
        "title": result.title,
        "source": result.source,
        "author": result.author,
        "year": result.year,
        "message": result.message,
    }


def cache_entry_to_result(entry: dict) -> ResolveResult:
    return ResolveResult(
        ok=bool(entry.get("ok")),
        registry=entry.get("registry"),
        title=entry.get("title"),
        source=entry.get("source"),
        author=entry.get("author"),
        year=entry.get("year"),
        message=entry.get("message", ""),
    )


# --------------------------------------------------------------------------
# Extraction
# --------------------------------------------------------------------------


def mask_non_content(text: str) -> str:
    """Blank out fenced code blocks and HTML comments, preserving line/offsets."""

    def blank(match: "re.Match[str]") -> str:
        return "".join(ch if ch == "\n" else " " for ch in match.group(0))

    text = CODE_FENCE_RE.sub(blank, text)
    text = HTML_COMMENT_RE.sub(blank, text)
    return text


def make_context(line: str, start: int, end: int) -> str:
    lo = max(0, start - CONTEXT_WINDOW)
    hi = min(len(line), end + CONTEXT_WINDOW)
    snippet = line[lo:hi].strip()
    prefix = "..." if lo > 0 else ""
    suffix = "..." if hi < len(line) else ""
    return f"{prefix}{snippet}{suffix}"


def clean_doi(raw: str) -> str:
    """Strip trailing sentence punctuation without eating real DOI characters.

    Trailing '.', ',', ';', ':' are always sentence punctuation and are
    stripped unconditionally. A trailing ')' is only stripped while it is
    unbalanced (more ')' than '(' in the candidate so far), since DOIs
    legitimately end in a balanced parenthetical (e.g. 10.1016/0304-3959
    (83)90164-1) that must survive while a sentence-closing paren tacked on
    after it must not. This loops until nothing more can be stripped, so a
    sentence-closing ')' following other punctuation (e.g. "...):") is
    peeled off in the right order.
    """
    doi = raw
    while doi:
        if doi[-1] in ".,;:":
            doi = doi[:-1]
            continue
        if doi[-1] == ")" and doi.count(")") > doi.count("("):
            doi = doi[:-1]
            continue
        break
    return doi


def extract_identifiers(file_label: str, text: str) -> List[Identifier]:
    masked = mask_non_content(text)
    lines = masked.split("\n")
    identifiers: List[Identifier] = []
    idx = 0

    for line_no, line in enumerate(lines, start=1):
        for m in DOI_RE.finditer(line):
            doi = clean_doi(m.group(0))
            if not doi:
                continue
            ctx = make_context(line, m.start(), m.start() + len(doi))
            identifiers.append(
                Identifier(
                    idx=idx,
                    id_type="doi",
                    normalised=doi,
                    display=f"doi:{doi}",
                    file=file_label,
                    line=line_no,
                    col=m.start(),
                    context=ctx,
                    expected_unverified=UNVERIFIED_MARKER in ctx,
                )
            )
            idx += 1

        for m in PMID_RE.finditer(line):
            pmid = m.group(1)
            ctx = make_context(line, m.start(), m.end())
            identifiers.append(
                Identifier(
                    idx=idx,
                    id_type="pmid",
                    normalised=pmid,
                    display=f"PMID {pmid}",
                    file=file_label,
                    line=line_no,
                    col=m.start(),
                    context=ctx,
                    expected_unverified=UNVERIFIED_MARKER in ctx,
                )
            )
            idx += 1

        for m in PMCID_RE.finditer(line):
            pmcid = m.group(0)
            numeric = pmcid[3:]
            ctx = make_context(line, m.start(), m.end())
            identifiers.append(
                Identifier(
                    idx=idx,
                    id_type="pmcid",
                    normalised=numeric,
                    display=pmcid,
                    file=file_label,
                    line=line_no,
                    col=m.start(),
                    context=ctx,
                    expected_unverified=UNVERIFIED_MARKER in ctx,
                )
            )
            idx += 1

        for pattern in (ARXIV_NEW_RE, ARXIV_OLD_RE):
            for m in pattern.finditer(line):
                arxiv_id = m.group(1)
                ctx = make_context(line, m.start(), m.end())
                identifiers.append(
                    Identifier(
                        idx=idx,
                        id_type="arxiv",
                        normalised=arxiv_id,
                        display=f"arXiv:{arxiv_id}",
                        file=file_label,
                        line=line_no,
                        col=m.start(),
                        context=ctx,
                        expected_unverified=UNVERIFIED_MARKER in ctx,
                    )
                )
                idx += 1

        for m in NCT_RE.finditer(line):
            nct = m.group(0)
            ctx = make_context(line, m.start(), m.end())
            identifiers.append(
                Identifier(
                    idx=idx,
                    id_type="nct",
                    normalised=nct,
                    display=nct,
                    file=file_label,
                    line=line_no,
                    col=m.start(),
                    context=ctx,
                    expected_unverified=UNVERIFIED_MARKER in ctx,
                )
            )
            idx += 1

        for m in ISBN_RE.finditer(line):
            isbn = m.group(1)
            ctx = make_context(line, m.start(), m.end())
            identifiers.append(
                Identifier(
                    idx=idx,
                    id_type="isbn",
                    normalised=isbn,
                    display=f"ISBN {isbn}",
                    file=file_label,
                    line=line_no,
                    col=m.start(),
                    context=ctx,
                    expected_unverified=UNVERIFIED_MARKER in ctx,
                )
            )
            idx += 1

    return identifiers


def find_doi_pmid_pairs(identifiers: List[Identifier]) -> List[Tuple[int, int]]:
    """Pair up DOI/PMID identifiers that sit next to each other on the same line.

    This is what catches a real DOI stitched to an unrelated real PMID: no
    per-identifier check sees that, only a comparison of what they resolve to.
    """
    by_line: Dict[int, List[Identifier]] = {}
    for ident in identifiers:
        if ident.id_type in ("doi", "pmid"):
            by_line.setdefault(ident.line, []).append(ident)

    pairs: List[Tuple[int, int]] = []
    for line_idents in by_line.values():
        dois = [i for i in line_idents if i.id_type == "doi"]
        pmids = [i for i in line_idents if i.id_type == "pmid"]
        candidates = []
        for d in dois:
            for p in pmids:
                dist = abs(d.col - p.col)
                if dist <= PAIR_PROXIMITY:
                    candidates.append((dist, d.idx, p.idx))
        candidates.sort()
        used: set = set()
        for _dist, d_idx, p_idx in candidates:
            if d_idx in used or p_idx in used:
                continue
            used.add(d_idx)
            used.add(p_idx)
            pairs.append((d_idx, p_idx))
    return pairs


def normalise_title(title: str) -> set:
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return set(w for w in title.split(" ") if w)


def normalise_title_tokens(title: str) -> List[str]:
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return [w for w in title.split(" ") if w]


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def titles_match(title_a: str, title_b: str) -> bool:
    """True if the titles should be treated as the same work.

    Crossref frequently stores a truncated title (main title only) while
    PubMed/DataCite store the full title including a subtitle, e.g.
    "Consciousness in the universe" vs "Consciousness in the universe: a
    review of the 'Orch OR' theory". A plain Jaccard word-overlap comparison
    scores that as a mismatch even though it is the same paper, so a
    prefix/containment check runs first: if the shorter (normalised) title's
    tokens are exactly the leading tokens of the longer one, it is a subtitle
    truncation, not a different paper, regardless of the Jaccard score. The
    3-token minimum stops a one- or two-word title from spuriously "matching"
    as a prefix of an unrelated longer title. Do not remove this in favour of
    "just use Jaccard": the threshold below is load-bearing for catching real
    DOI/PMID mismatches, so this containment check has to be resolved before
    Jaccard, not folded into it.
    """
    tokens_a = normalise_title_tokens(title_a)
    tokens_b = normalise_title_tokens(title_b)
    shorter, longer = (tokens_a, tokens_b) if len(tokens_a) <= len(tokens_b) else (tokens_b, tokens_a)
    if len(shorter) >= 3 and longer[: len(shorter)] == shorter:
        return True
    return jaccard(set(tokens_a), set(tokens_b)) >= MISMATCH_THRESHOLD


# --------------------------------------------------------------------------
# Resolvers
# --------------------------------------------------------------------------


_HTML_TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(text: Optional[str]) -> Optional[str]:
    """Strip embedded JATS/HTML markup that some publishers ship inside
    Crossref title fields (e.g. '<scp>' small-caps tags), which would
    otherwise corrupt both the display and the title cross-check."""
    if text is None:
        return None
    return _HTML_TAG_RE.sub("", text).strip()


def _load_json_or_raise_unreachable(body: bytes, registry: str) -> dict:
    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        raise NetworkError(f"malformed JSON from {registry} (HTTP 200)") from exc


def resolve_doi_datacite(
    doi: str, limiters: Dict[str, RateLimiter], headers: Dict[str, str], timeout: float
) -> ResolveResult:
    url = f"https://api.datacite.org/dois/{urllib.parse.quote(doi, safe='/:();')}"
    try:
        status, body = http_get(url, headers, limiters["api.datacite.org"], timeout)
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=f"UNREACHABLE after 3 attempts ({exc})")
    if status == 404:
        return ResolveResult(ok=False, message="not found in Crossref or DataCite")
    if status != 200:
        return ResolveResult(ok=False, message=f"DataCite returned HTTP {status}")
    try:
        data = _load_json_or_raise_unreachable(body, "DataCite")
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=str(exc))
    attrs = (data.get("data") or {}).get("attributes") or {}
    titles = attrs.get("titles") or []
    title = titles[0].get("title") if titles and isinstance(titles[0], dict) else None
    title = strip_tags(title)
    if not title:
        return ResolveResult(ok=False, message="not found in Crossref or DataCite")
    year = attrs.get("publicationYear")
    creators = attrs.get("creators") or []
    author = None
    if creators and isinstance(creators[0], dict):
        author = creators[0].get("familyName") or creators[0].get("name")
    return ResolveResult(
        ok=True,
        registry="datacite",
        title=title,
        source=strip_tags(attrs.get("publisher")),
        author=strip_tags(author),
        year=str(year) if year else None,
    )


def resolve_doi(
    doi: str, limiters: Dict[str, RateLimiter], headers: Dict[str, str], timeout: float
) -> ResolveResult:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/:();')}"
    try:
        status, body = http_get(url, headers, limiters["api.crossref.org"], timeout)
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=f"UNREACHABLE after 3 attempts ({exc})")
    if status == 404:
        return resolve_doi_datacite(doi, limiters, headers, timeout)
    if status != 200:
        return ResolveResult(ok=False, message=f"Crossref returned HTTP {status}")
    try:
        data = _load_json_or_raise_unreachable(body, "Crossref")
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=str(exc))
    msg = data.get("message") if isinstance(data, dict) else None
    if not isinstance(msg, dict):
        return ResolveResult(ok=False, unreachable=True, message="unexpected Crossref response shape")
    titles = msg.get("title") or []
    title = strip_tags(titles[0] if titles else None)
    if not title:
        return ResolveResult(ok=False, message="Crossref record has no title")
    containers = msg.get("container-title") or []
    source = strip_tags(containers[0] if containers else None)
    year = None
    date_parts = ((msg.get("issued") or {}).get("date-parts") or [[]])
    if date_parts and date_parts[0]:
        year = date_parts[0][0]
    authors = msg.get("author") or []
    author = authors[0].get("family") if authors and isinstance(authors[0], dict) else None
    return ResolveResult(
        ok=True,
        registry="crossref",
        title=title,
        source=source,
        author=strip_tags(author),
        year=str(year) if year else None,
    )


def resolve_esummary(
    db: str,
    uid: str,
    display_registry: str,
    limiters: Dict[str, RateLimiter],
    headers: Dict[str, str],
    timeout: float,
    api_key: Optional[str],
    not_found_message: str,
) -> ResolveResult:
    params = f"db={db}&id={uid}&retmode=json"
    if api_key:
        params += f"&api_key={urllib.parse.quote(api_key)}"
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?{params}"
    try:
        status, body = http_get(url, headers, limiters["eutils.ncbi.nlm.nih.gov"], timeout)
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=f"UNREACHABLE after 3 attempts ({exc})")
    if status != 200:
        return ResolveResult(ok=False, message=f"NCBI ESummary returned HTTP {status}")
    try:
        data = _load_json_or_raise_unreachable(body, "NCBI ESummary")
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=str(exc))
    result = data.get("result") if isinstance(data, dict) else None
    if not isinstance(result, dict):
        return ResolveResult(ok=False, unreachable=True, message="unexpected NCBI ESummary response shape")
    rec = result.get(str(uid))
    if not isinstance(rec, dict) or rec.get("error") or not rec.get("title"):
        return ResolveResult(ok=False, message=not_found_message)
    title = strip_tags(str(rec.get("title", "")).rstrip("."))
    source = strip_tags(rec.get("source"))
    authors = rec.get("authors") or []
    author = authors[0].get("name") if authors and isinstance(authors[0], dict) else None
    year_match = re.search(r"\d{4}", str(rec.get("pubdate", "")))
    year = year_match.group(0) if year_match else None
    return ResolveResult(
        ok=True, registry=display_registry, title=title, source=source, author=author, year=year
    )


def resolve_pmid(
    pmid: str, limiters: Dict[str, RateLimiter], headers: Dict[str, str], timeout: float, api_key: Optional[str]
) -> ResolveResult:
    return resolve_esummary(
        "pubmed", pmid, "pubmed", limiters, headers, timeout, api_key, "not found in PubMed"
    )


def resolve_pmcid(
    numeric: str, limiters: Dict[str, RateLimiter], headers: Dict[str, str], timeout: float, api_key: Optional[str]
) -> ResolveResult:
    return resolve_esummary(
        "pmc", numeric, "pmc", limiters, headers, timeout, api_key, "not found in PMC"
    )


def resolve_arxiv(
    arxiv_id: str, limiters: Dict[str, RateLimiter], headers: Dict[str, str], timeout: float
) -> ResolveResult:
    url = f"http://export.arxiv.org/api/query?id_list={urllib.parse.quote(arxiv_id)}"
    try:
        status, body = http_get(url, headers, limiters["export.arxiv.org"], timeout)
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=f"UNREACHABLE after 3 attempts ({exc})")
    if status != 200:
        return ResolveResult(ok=False, message=f"arXiv API returned HTTP {status}")
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return ResolveResult(ok=False, unreachable=True, message="malformed XML from arXiv (HTTP 200)")
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries = root.findall("atom:entry", ns)
    if len(entries) != 1:
        return ResolveResult(ok=False, message="not found on arXiv")
    entry = entries[0]
    title_el = entry.find("atom:title", ns)
    title = title_el.text.strip() if title_el is not None and title_el.text else None
    if not title or title.strip().lower() == "error":
        return ResolveResult(ok=False, message="not found on arXiv")
    published_el = entry.find("atom:published", ns)
    year = published_el.text[:4] if published_el is not None and published_el.text else None
    author_el = entry.find("atom:author/atom:name", ns)
    author = author_el.text if author_el is not None else None
    return ResolveResult(ok=True, registry="arxiv", title=title, author=author, year=year)


def resolve_nct(
    nct: str, limiters: Dict[str, RateLimiter], headers: Dict[str, str], timeout: float
) -> ResolveResult:
    url = f"https://clinicaltrials.gov/api/v2/studies/{nct}?fields=NCTId,BriefTitle,OverallStatus"
    try:
        status, body = http_get(url, headers, limiters["clinicaltrials.gov"], timeout)
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=f"UNREACHABLE after 3 attempts ({exc})")
    if status == 404:
        return ResolveResult(ok=False, message="not found in ClinicalTrials.gov")
    if status != 200:
        return ResolveResult(ok=False, message=f"ClinicalTrials.gov returned HTTP {status}")
    try:
        data = _load_json_or_raise_unreachable(body, "ClinicalTrials.gov")
    except NetworkError as exc:
        return ResolveResult(ok=False, unreachable=True, message=str(exc))
    ident = ((data.get("protocolSection") or {}).get("identificationModule")) or {}
    nct_id = ident.get("nctId")
    if not nct_id or nct_id.upper() != nct.upper():
        return ResolveResult(ok=False, message="not found in ClinicalTrials.gov")
    status_mod = ((data.get("protocolSection") or {}).get("statusModule")) or {}
    return ResolveResult(
        ok=True,
        registry="clinicaltrials.gov",
        title=ident.get("briefTitle"),
        source=status_mod.get("overallStatus"),
    )


def resolve_one(
    id_type: str,
    normalised: str,
    limiters: Dict[str, RateLimiter],
    headers: Dict[str, str],
    timeout: float,
    ncbi_api_key: Optional[str],
) -> ResolveResult:
    if id_type == "doi":
        return resolve_doi(normalised, limiters, headers, timeout)
    if id_type == "pmid":
        return resolve_pmid(normalised, limiters, headers, timeout, ncbi_api_key)
    if id_type == "pmcid":
        return resolve_pmcid(normalised, limiters, headers, timeout, ncbi_api_key)
    if id_type == "arxiv":
        return resolve_arxiv(normalised, limiters, headers, timeout)
    if id_type == "nct":
        return resolve_nct(normalised, limiters, headers, timeout)
    raise ValueError(f"no resolver for identifier type {id_type!r}")


def cache_key(id_type: str, normalised: str) -> str:
    if id_type == "doi":
        return f"doi:{normalised.lower()}"
    if id_type == "nct":
        return f"nct:{normalised.upper()}"
    return f"{id_type}:{normalised}"


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------


def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / ".git").exists():
            return candidate
    return start


def collect_markdown_files(paths: List[str]) -> List[Path]:
    files: List[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            files.append(p)
        else:
            print(f"warning: path not found, skipping: {raw}", file=sys.stderr)
    return files


def format_metadata(result: ResolveResult) -> str:
    parts = []
    if result.title:
        title = result.title
        detail_bits = []
        if result.source:
            detail_bits.append(result.source)
        if result.year:
            detail_bits.append(str(result.year))
        detail = ", ".join(detail_bits)
        parts.append(f"{title} ({detail})" if detail else title)
    if result.registry:
        parts.append(f"[{result.registry}]")
    return " ".join(parts) if parts else result.message


def build_findings(
    identifiers: List[Identifier],
    results: Dict[str, ResolveResult],
    pairs: List[Tuple[int, int]],
) -> List[Finding]:
    by_idx = {i.idx: i for i in identifiers}
    findings: Dict[int, Finding] = {}

    for ident in identifiers:
        if ident.id_type == "isbn":
            findings[ident.idx] = Finding(ident, "skip", "not checkable")
            continue

        result = results[cache_key(ident.id_type, ident.normalised)]

        if ident.expected_unverified:
            if result.ok:
                findings[ident.idx] = Finding(
                    ident,
                    "warn",
                    f"resolves despite [UNVERIFIED] marker: {format_metadata(result)}"
                    " (consider removing the marker)",
                )
            else:
                findings[ident.idx] = Finding(
                    ident, "skip", "marked [UNVERIFIED]; not resolved, as expected"
                )
            continue

        if result.unreachable:
            findings[ident.idx] = Finding(ident, "warn", result.message)
        elif result.ok:
            findings[ident.idx] = Finding(ident, "ok", format_metadata(result))
        else:
            findings[ident.idx] = Finding(
                ident,
                "FAIL",
                result.message,
                detail=f'L{ident.line}: "{ident.context}"',
            )

    # Cross-check: DOI/PMID pairs whose resolved titles disagree.
    for a_idx, b_idx in pairs:
        a = by_idx[a_idx]
        b = by_idx[b_idx]
        finding_a = findings.get(a_idx)
        finding_b = findings.get(b_idx)
        if finding_a is None or finding_b is None:
            continue
        if finding_a.status != "ok" or finding_b.status != "ok":
            continue
        result_a = results[cache_key(a.id_type, a.normalised)]
        result_b = results[cache_key(b.id_type, b.normalised)]
        if not result_a.title or not result_b.title:
            continue
        overlap = jaccard(normalise_title(result_a.title), normalise_title(result_b.title))
        if not titles_match(result_a.title, result_b.title):
            message = (
                f"MISMATCH vs {b.display}: titles disagree (overlap {overlap:.2f}): "
                f"'{result_a.title}' vs '{result_b.title}'"
            )
            detail = f'L{a.line}: "{a.context}"'
            findings[a_idx] = Finding(a, "MISMATCH", message, detail=detail)
            message_b = (
                f"MISMATCH vs {a.display}: titles disagree (overlap {overlap:.2f}): "
                f"'{result_b.title}' vs '{result_a.title}'"
            )
            findings[b_idx] = Finding(b, "MISMATCH", message_b, detail=f'L{b.line}: "{b.context}"')

    return [findings[i.idx] for i in identifiers]


def resolve_all(
    identifiers: List[Identifier],
    cache: Cache,
    limiters: Dict[str, RateLimiter],
    headers: Dict[str, str],
    timeout: float,
    jobs: int,
    ncbi_api_key: Optional[str],
) -> Dict[str, ResolveResult]:
    targets: Dict[str, Tuple[str, str]] = {}
    for ident in identifiers:
        if ident.id_type == "isbn":
            continue
        key = cache_key(ident.id_type, ident.normalised)
        targets.setdefault(key, (ident.id_type, ident.normalised))

    results: Dict[str, ResolveResult] = {}
    to_fetch: List[Tuple[str, str, str]] = []
    for key, (id_type, normalised) in targets.items():
        cached = cache.get(key)
        if cached is not None:
            results[key] = cache_entry_to_result(cached)
        else:
            to_fetch.append((key, id_type, normalised))

    def _work(item: Tuple[str, str, str]) -> Tuple[str, ResolveResult]:
        key, id_type, normalised = item
        result = resolve_one(id_type, normalised, limiters, headers, timeout, ncbi_api_key)
        return key, result

    if to_fetch:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
            for key, result in pool.map(_work, to_fetch):
                results[key] = result
                if not result.unreachable:
                    cache.put(key, result_to_cache_entry(result))

    return results


STATUS_ORDER = {"ok": 0, "skip": 1, "warn": 2, "FAIL": 3, "MISMATCH": 3}


def print_human_report(
    file_findings: "List[Tuple[str, List[Finding]]]", quiet: bool
) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for file_label, findings in file_findings:
        print(file_label)
        if not findings:
            print("  no identifiers found")
            print()
            continue
        for f in findings:
            counts[f.status] = counts.get(f.status, 0) + 1
            if quiet and f.status == "ok":
                continue
            print(f"  {f.status:<5}{f.identifier.line:>4}  {f.identifier.display:<28} {f.info}")
            if f.detail:
                print(f"        {f.detail}")
        print()
    return counts


def print_json_report(file_findings: "List[Tuple[str, List[Finding]]]") -> Dict[str, int]:
    counts: Dict[str, int] = {}
    out = {"files": {}}
    for file_label, findings in file_findings:
        entries = []
        for f in findings:
            counts[f.status] = counts.get(f.status, 0) + 1
            entries.append(
                {
                    "type": f.identifier.id_type,
                    "id": f.identifier.normalised,
                    "display": f.identifier.display,
                    "line": f.identifier.line,
                    "status": f.status,
                    "info": f.info,
                    "context": f.identifier.context,
                    "detail": f.detail,
                }
            )
        out["files"][file_label] = entries
    out["summary"] = counts
    print(json.dumps(out, indent=2))
    return counts


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify that identifiers cited in markdown resolve against their registries."
    )
    parser.add_argument("files", nargs="*", help="markdown files or directories (default: evidence/ conjectures/)")
    parser.add_argument("--cache", default=None, help="cache file path (default: <repo root>/.citation-cache.json)")
    parser.add_argument("--no-cache", action="store_true", help="bypass cache read and write")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT, help="per-request timeout in seconds")
    parser.add_argument("--jobs", type=int, default=DEFAULT_JOBS, help="parallel resolver workers")
    parser.add_argument("--json", action="store_true", help="print a machine-readable report")
    parser.add_argument("--quiet", action="store_true", help="omit ok lines from the human report")
    parser.add_argument(
        "--allow-unverified",
        action="store_true",
        help="downgrade failures to warnings; always exit 0",
    )
    parser.add_argument(
        "--strict-network",
        action="store_true",
        help="treat UNREACHABLE identifiers as build failures instead of warnings",
    )
    args = parser.parse_args(argv)

    repo_root = find_repo_root(Path.cwd())

    if args.files:
        input_paths = args.files
    else:
        input_paths = [str(repo_root / "evidence"), str(repo_root / "conjectures")]

    md_files = collect_markdown_files(input_paths)

    cache_path = Path(args.cache) if args.cache else (repo_root / DEFAULT_CACHE_NAME)
    cache = Cache(cache_path, enabled=not args.no_cache)

    mailto = os.environ.get("CROSSREF_MAILTO", "research@example.org")
    ncbi_api_key = os.environ.get("NCBI_API_KEY") or None
    headers = make_headers(mailto)
    limiters = build_limiters(ncbi_api_key)

    file_findings: List[Tuple[str, List[Finding]]] = []

    for path in md_files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"error: could not read {path}: {exc}", file=sys.stderr)
            continue

        file_label = str(path)
        if not text.strip():
            file_findings.append((file_label, []))
            continue

        identifiers = extract_identifiers(file_label, text)
        if not identifiers:
            file_findings.append((file_label, []))
            continue

        pairs = find_doi_pmid_pairs(identifiers)
        results = resolve_all(
            identifiers, cache, limiters, headers, args.timeout, args.jobs, ncbi_api_key
        )
        findings = build_findings(identifiers, results, pairs)
        file_findings.append((file_label, findings))

    cache.save()

    if args.strict_network:
        for _label, findings in file_findings:
            for f in findings:
                if f.status == "warn" and "UNREACHABLE" in f.info:
                    f.status = "FAIL"

    if args.json:
        counts = print_json_report(file_findings)
    else:
        counts = print_human_report(file_findings, args.quiet)
        total = sum(counts.values())
        summary_bits = ", ".join(f"{status}={counts.get(status, 0)}" for status in ("ok", "FAIL", "MISMATCH", "warn", "skip") if counts.get(status))
        print(f"Summary: {total} identifiers checked ({summary_bits or 'none'})")

    fail_count = counts.get("FAIL", 0) + counts.get("MISMATCH", 0)

    if args.allow_unverified:
        if fail_count and not args.json:
            print("--allow-unverified set: failures downgraded, exiting 0.")
        return 0

    return 1 if fail_count else 0


if __name__ == "__main__":
    sys.exit(main())
