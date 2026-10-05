#!/usr/bin/env python3
"""Passive security-header, cookie and well-known-file checker.

Sends only normal GET/HEAD requests (like a browser visit). Use on sites you own
or are authorized to assess.

Usage: python3 check_headers.py https://www.example.com [--json out.json]
"""
import argparse, json, re, ssl, sys, urllib.request, urllib.error
from urllib.parse import urlparse, urlunparse

UA = "Mozilla/5.0 (security-audit skill; Mahara AI)"

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None

def fetch(url, method="GET", follow=True, timeout=20):
    handlers = [] if follow else [NoRedirect()]
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        r = opener.open(req, timeout=timeout)
        body = r.read(200_000) if method == "GET" else b""
        return r.status, r.headers, body, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, e.headers, b"", url
    except Exception as e:  # network/TLS
        return None, None, str(e).encode(), url

def check(url):
    results, score = [], 100
    def add(check_id, status, severity, detail, penalty=0):
        nonlocal score
        results.append({"id": check_id, "status": status, "severity": severity, "detail": detail})
        if status != "pass":
            score -= penalty

    status, h, body, final = fetch(url)
    if status is None:
        return {"url": url, "error": body.decode(errors="ignore")}
    get = lambda k: h.get(k) if h else None

    # HTTPS redirect
    p = urlparse(url)
    http_url = urlunparse(("http", p.netloc, p.path or "/", "", "", ""))
    s2, h2, _, _ = fetch(http_url, follow=False)
    loc = (h2.get("Location") if h2 else "") or ""
    if s2 in (301, 302, 307, 308) and loc.startswith("https://"):
        add("https_redirect", "pass", "info", f"HTTP -> {loc}")
    else:
        add("https_redirect", "fail", "high", f"HTTP responded {s2} without HTTPS redirect", 10)

    hsts = get("Strict-Transport-Security")
    if hsts and re.search(r"max-age=(\d+)", hsts) and int(re.search(r"max-age=(\d+)", hsts).group(1)) >= 15552000:
        add("hsts", "pass", "info", hsts)
    else:
        add("hsts", "warn", "medium", f"HSTS missing or max-age < 180 days: {hsts}", 5)

    csp = get("Content-Security-Policy")
    csp_ro = get("Content-Security-Policy-Report-Only")
    if csp:
        weak = [t for t in ("'unsafe-inline'", "'unsafe-eval'") if re.search(r"script-src[^;]*" + re.escape(t), csp) or
                (t in csp and "script-src" not in csp)]
        if weak:
            add("csp", "warn", "medium", f"CSP present but script-src allows {', '.join(weak)}", 10)
        else:
            add("csp", "pass", "info", csp[:300])
    else:
        add("csp", "fail", "medium", "No enforcing Content-Security-Policy" + (" (Report-Only present)" if csp_ro else ""), 25)

    xfo = get("X-Frame-Options")
    fa = csp and "frame-ancestors" in csp
    if xfo or fa:
        add("clickjacking", "pass", "info", f"XFO={xfo} frame-ancestors={'yes' if fa else 'no'}")
    else:
        add("clickjacking", "fail", "medium", "Neither X-Frame-Options nor CSP frame-ancestors", 20)

    for hid, name, want, sev, pen in [
        ("xcto", "X-Content-Type-Options", "nosniff", "low", 10),
        ("referrer", "Referrer-Policy", None, "low", 10),
        ("permissions", "Permissions-Policy", None, "low", 5),
        ("coop", "Cross-Origin-Opener-Policy", None, "low", 5),
    ]:
        v = get(name)
        if v and (want is None or v.strip().lower() == want):
            if hid == "referrer" and v.strip().lower() in ("unsafe-url", "no-referrer-when-downgrade"):
                add(hid, "warn", sev, f"{name}: {v} (leaks full URLs)", pen)
            else:
                add(hid, "pass", "info", f"{name}: {v}")
        else:
            add(hid, "fail", sev, f"{name} missing or wrong: {v}", pen)

    for leak in ("Server", "X-Powered-By", "X-AspNet-Version"):
        v = get(leak)
        if v and (leak != "Server" or re.search(r"\d", v)):
            add(f"disclosure_{leak.lower()}", "warn", "low", f"{leak}: {v} reveals technology/version", 2)

    cookies = h.get_all("Set-Cookie") or [] if h else []
    for c in cookies:
        name = c.split("=", 1)[0].strip()
        attrs = c.lower()
        missing = [a for a, k in (("Secure", "secure"), ("HttpOnly", "httponly"), ("SameSite", "samesite")) if k not in attrs]
        if missing:
            sensitive = re.search(r"sess|auth|token|jwt|sid|next-auth|supabase", name, re.I)
            sev = "high" if sensitive else "low"
            add(f"cookie_{name}", "warn", sev,
                f"Cookie {name} missing {', '.join(missing)}" + ("" if sensitive else " (looks non-sensitive; HttpOnly optional if JS reads it)"),
                8 if sensitive else 3)
        else:
            add(f"cookie_{name}", "pass", "info", f"Cookie {name} has Secure, HttpOnly, SameSite")

    base = f"{p.scheme}://{p.netloc}"
    for path, cid, sev in [("/.well-known/security.txt", "security_txt", "info"), ("/robots.txt", "robots_txt", "info"),
                           ("/site.webmanifest", "webmanifest", "info"), ("/manifest.webmanifest", "webmanifest_alt", "info"),
                           ("/humans.txt", "humans_txt", "info")]:
        st, hh, b, _ = fetch(base + path)
        ctype = (hh.get("Content-Type") if hh else "") or ""
        ok = st == 200 and "text/html" not in ctype.lower()
        if cid == "security_txt" and ok and b"expires:" not in b.lower():
            add(cid, "warn", "info", f"{path} present but missing required Expires field")
        else:
            add(cid, "pass" if ok else "missing", sev, f"{path} -> {st} {ctype}")

    html = body.decode(errors="ignore") if body else ""
    add("canonical", "pass" if re.search(r'<link[^>]+rel=["\']canonical', html, re.I) else "missing", "info", "canonical link tag")

    score = max(0, score)
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 65 else "D" if score >= 50 else "F"
    return {"url": url, "final_url": final, "status": status, "score": score, "grade": grade, "checks": results}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--json")
    a = ap.parse_args()
    url = a.url if a.url.startswith("http") else "https://" + a.url
    r = check(url)
    if "error" in r:
        print(f"ERROR fetching {url}: {r['error']}"); sys.exit(2)
    print(f"{r['url']}  ->  grade {r['grade']} ({r['score']}/100)")
    for c in r["checks"]:
        mark = {"pass": "PASS", "fail": "FAIL", "warn": "WARN", "missing": "MISS"}[c["status"]]
        print(f"  [{mark}] {c['id']:<22} {c['severity']:<6} {c['detail']}")
    if a.json:
        with open(a.json, "w") as f: json.dump(r, f, indent=2)
        print(f"JSON written to {a.json}")

if __name__ == "__main__":
    main()
