#!/usr/bin/env python3
"""Reader's tool for P-004. Standard library only.

It holds no identifier of the paper. Addresses are passed on the command line.

  python3 -I reader_routes.py get LABEL URL OUTDIR
      ONE scripted request, as REGISTRATION.md section 5 states it: the fixed
      user-agent, no cookies, no other header chosen by the reader, redirects
      followed inside the request. The body is saved as OUTDIR/LABEL.body and
      one JSON line is appended to OUTDIR/requests.jsonl: start time (UTC),
      address requested, HTTP status, Content-Type, final address, redirect
      hops, size in bytes. If no HTTP response comes back, that is logged as
      "no HTTP response" and nothing is retried by this tool.

  python3 -I reader_routes.py select HTMLFILE CONTENT_TYPE REQUESTED_A FINAL_A [ANSWERED ...]
      Route 5, step (b): the mechanical choice of the one link to request from
      an HTML landing page. HTMLFILE is the saved body of (a). CONTENT_TYPE is
      the Content-Type header of (a). REQUESTED_A and FINAL_A are the address
      requested in (a) and the address (a) ended at. ANSWERED are the
      addresses already requested in this attempt that received an HTTP
      response. Prints a JSON report: the links, which qualified and why,
      which were excluded and under which exclusion, and the first candidate
      in document order, or that none remains.

  python3 -I reader_routes.py selftest
      Checks the selection against small synthetic pages. No network.
"""
import datetime
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

USER_AGENT = "research-reader/1.0 (scripted; one request per step)"
TIMEOUT_S = 60


# ---------------------------------------------------------------- requests

class _Hops(urllib.request.HTTPRedirectHandler):
    """Follows redirects as urllib does by default, and records each hop."""

    def __init__(self):
        self.hops = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.hops.append({"status": code, "to": newurl})
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def get(label, url, outdir):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    hops = _Hops()
    # build_opener adds no cookie handling: no cookie is stored or sent.
    opener = urllib.request.build_opener(hops)
    opener.addheaders = [("User-Agent", USER_AGENT)]
    rec = {
        "label": label,
        "time_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "requested": url,
    }
    try:
        try:
            resp = opener.open(url, timeout=TIMEOUT_S)
        except urllib.error.HTTPError as err:  # an HTTP response with an error status
            resp = err
        body = resp.read()
        rec.update(
            status=resp.status if hasattr(resp, "status") else resp.code,
            content_type=resp.headers.get("Content-Type"),
            final=resp.geturl(),
            hops=hops.hops,
            size=len(body),
            first_bytes=body[:8].decode("latin-1"),
        )
        (outdir / f"{label}.body").write_bytes(body)
    except Exception as err:  # no HTTP response at all
        rec.update(status=None, error=f"no HTTP response: {type(err).__name__}: {err}",
                   hops=hops.hops)
    with open(outdir / "requests.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    return 0


# --------------------------------------------------------------- selection

class _Links(HTMLParser):
    """Start tags only. html.parser does not report tags inside comments or
    inside script elements, so those are not links."""

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = {}
        for k, v in attrs:
            a.setdefault(k.lower(), v)
        if tag in ("a", "link"):
            value, element = a.get("href"), tag
        elif tag == "meta" and (a.get("name") or "").lower() == "citation_pdf_url":
            value, element = a.get("content"), "meta[citation_pdf_url]"
        else:
            return
        if not value:
            return
        self.links.append({
            "element": element,
            "raw": value,
            "type_attr": a.get("type"),
            "line": self.getpos()[0],
        })


def decode_body(body, content_type):
    m = re.search(r"charset\s*=\s*\"?([^\";\s]+)", content_type or "", re.IGNORECASE)
    charset = m.group(1) if m else "utf-8"
    try:
        return body.decode(charset, errors="replace")
    except LookupError:
        return body.decode("utf-8", errors="replace")


def select(html_text, requested_a, final_a, answered):
    parser = _Links()
    parser.feed(html_text)
    parser.close()
    host_a = (urllib.parse.urlparse(final_a).hostname or "").lower()
    report, candidate = [], None
    for n, link in enumerate(parser.links):
        resolved = urllib.parse.urldefrag(urllib.parse.urljoin(final_a, link["raw"]))[0]
        parts = urllib.parse.urlparse(resolved)
        path = parts.path.lower()
        why = []
        if path.endswith(".pdf"):
            why.append("path ends in .pdf")
        if "fulltext" in path:
            why.append("path contains fulltext")
        if link["type_attr"] == "application/pdf":
            why.append('type="application/pdf"')
        if link["element"] == "meta[citation_pdf_url]":
            why.append("citation_pdf_url")
        if not why:
            continue
        excluded = []
        if resolved == requested_a or resolved == final_a:
            excluded.append("equals the address of (a) or its final address")
        host = parts.hostname
        if not host or host.lower() != host_a:
            excluded.append("different host")
        if resolved in answered:
            excluded.append("already requested and answered in this attempt")
        entry = {
            "order": n,
            "line": link["line"],
            "element": link["element"],
            "resolved": resolved,
            "qualifies_by": why,
            "excluded_by": excluded,
        }
        report.append(entry)
        if not excluded and candidate is None:
            candidate = entry
    return {
        "links_total": len(parser.links),
        "qualifying": len(report),
        "excluded": sum(1 for e in report if e["excluded_by"]),
        "qualifying_links": report,
        "requested_in_b": candidate,
    }


def select_cmd(html_file, content_type, requested_a, final_a, answered):
    text = decode_body(Path(html_file).read_bytes(), content_type)
    print(json.dumps(select(text, requested_a, final_a, set(answered)),
                     ensure_ascii=False, indent=1))
    return 0


def selftest():
    final = "https://repo.example.org/record/1?x=1"
    page = """<html><head><base href="https://elsewhere.example.org/">
    <!-- <a href="/in-comment.pdf">no</a> -->
    <script>var s = '<a href="/in-script.pdf">no</a>';</script>
    <link rel="canonical" href="/record/1?x=1#top">
    <link rel="alternate" type="application/pdf" href="https://cdn.example.org/f/1">
    <meta name="Citation_PDF_URL" content="">
    </head><body>
    <a href="mailto:a@example.org?subject=x.pdf">m</a>
    <a href="/about">about</a>
    <a href="/FullText/again">already answered</a>
    <a href="files/Paper.PDF;v=2?download=1#p3">first candidate</a>
    <a href="/second.pdf">second</a>
    <meta name="citation_pdf_url" content="/third.pdf">
    </body></html>"""
    out = select(page, "https://repo.example.org/h/1", final,
                 {"https://repo.example.org/FullText/again"})
    got = out["requested_in_b"]["resolved"] if out["requested_in_b"] else None
    want = "https://repo.example.org/record/files/Paper.PDF;v=2?download=1"
    checks = [
        ("first candidate, parameters and query kept, fragment stripped, base ignored",
         got == want),
        ("comment and script links are not links",
         not any("in-" in e["resolved"] for e in out["qualifying_links"])),
        ("other host excluded", any(e["excluded_by"] == ["different host"]
                                    and "cdn." in e["resolved"] for e in out["qualifying_links"])),
        ("answered address excluded", any(
            "already requested and answered in this attempt" in e["excluded_by"]
            for e in out["qualifying_links"])),
        ("counts", (out["qualifying"], out["excluded"]) == (5, 2)),
    ]
    own = select('<a href="/h/1.pdf">self</a><a href="/x">x</a>',
                 "https://repo.example.org/h/1.pdf", "https://repo.example.org/h/1.pdf", set())
    checks.append(("a link to the page itself is excluded and no candidate remains",
                   own["requested_in_b"] is None and own["excluded"] == 1))
    none = select('<a href="/x">x</a>', final, final, set())
    checks.append(("no qualifying link, no candidate", none["requested_in_b"] is None))
    bad = 0
    for name, ok in checks:
        print(("ok    " if ok else "FAIL  ") + name)
        bad += 0 if ok else 1
    print("FAIL" if bad else f"PASS  {len(checks)} of {len(checks)}")
    return 1 if bad else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 4 and args[0] == "get":
        sys.exit(get(args[1], args[2], args[3]))
    if len(args) >= 5 and args[0] == "select":
        sys.exit(select_cmd(args[1], args[2], args[3], args[4], args[5:]))
    if args == ["selftest"]:
        sys.exit(selftest())
    print(__doc__)
    sys.exit(2)
