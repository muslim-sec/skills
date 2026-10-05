#!/usr/bin/env python3
"""
Maharat-SEO — page analyzer (no network).

IMPORTANT: This script does NOT fetch URLs. Fetch page HTML, robots.txt,
sitemap.xml and llms.txt with the web_fetch tool first, save them to files,
then run this analyzer on the saved files. It parses the SEO/AEO signals that
are tedious to eyeball and emits structured JSON for the report/dashboard.

Usage:
  python3 audit.py --html page.html [--url https://site.com/page] \
      [--robots robots.txt] [--sitemap sitemap.xml] [--llms llms.txt] \
      [--out signals.json]

Stdlib only (html.parser, re, json, argparse). Python 3.8+.
"""
import argparse, json, re, sys
from html.parser import HTMLParser

AI_CRAWLERS = {
    "gptbot": ("OpenAI", "ChatGPT training"),
    "oai-searchbot": ("OpenAI", "ChatGPT search"),
    "chatgpt-user": ("OpenAI", "ChatGPT browsing"),
    "claudebot": ("Anthropic", "Claude web"),
    "anthropic-ai": ("Anthropic", "Claude training"),
    "perplexitybot": ("Perplexity", "Perplexity search"),
    "perplexity-user": ("Perplexity", "Perplexity fetch"),
    "google-extended": ("Google", "Gemini training"),
    "googlebot": ("Google", "Search + AIO"),
    "bingbot": ("Microsoft", "Bing + Copilot"),
    "ccbot": ("Common Crawl", "training"),
    "bytespider": ("ByteDance", "TikTok AI"),
    "cohere-ai": ("Cohere", "Cohere models"),
}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None
        self._in_title = False
        self.metas = []           # list of dicts of attrs
        self.headings = []        # (level, text)
        self._cur_h = None
        self._h_buf = []
        self.links = []           # (href, rel, text)
        self._cur_a = None
        self._a_buf = []
        self.images = []          # (src, alt_present, alt_text)
        self.jsonld = []          # raw script contents
        self._in_ld = False
        self._ld_buf = []
        self.canonical = None
        self.html_lang = None
        self.body_text_len = 0
        self.script_count = 0
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html" and a.get("lang"):
            self.html_lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            self.metas.append(a)
            if a.get("name", "").lower() == "viewport":
                self.has_viewport = True
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            if "canonical" in rel:
                self.canonical = a.get("href")
        elif tag in ("h1", "h2", "h3", "h4"):
            self._cur_h = int(tag[1]); self._h_buf = []
        elif tag == "a":
            self._cur_a = (a.get("href"), (a.get("rel") or "")); self._a_buf = []
        elif tag == "img":
            self.images.append((a.get("src"), "alt" in a, a.get("alt", "")))
        elif tag == "script":
            self.script_count += 1
            if (a.get("type") or "").lower() == "application/ld+json":
                self._in_ld = True; self._ld_buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3", "h4") and self._cur_h:
            txt = " ".join("".join(self._h_buf).split())
            if txt:
                self.headings.append((self._cur_h, txt))
            self._cur_h = None
        elif tag == "a" and self._cur_a is not None:
            txt = " ".join("".join(self._a_buf).split())
            self.links.append((self._cur_a[0], self._cur_a[1], txt))
            self._cur_a = None
        elif tag == "script" and self._in_ld:
            self.jsonld.append("".join(self._ld_buf)); self._in_ld = False

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data
        if self._cur_h:
            self._h_buf.append(data)
        if self._cur_a is not None:
            self._a_buf.append(data)
        if self._in_ld:
            self._ld_buf.append(data)
        self.body_text_len += len(data.strip())


def meta_get(metas, name=None, prop=None):
    for m in metas:
        if name and m.get("name", "").lower() == name.lower():
            return m.get("content")
        if prop and m.get("property", "").lower() == prop.lower():
            return m.get("content")
    return None


def analyze_page(html, url=None):
    p = PageParser()
    try:
        p.feed(html)
    except Exception as e:
        pass
    title = (p.title or "").strip()
    desc = meta_get(p.metas, name="description")
    robots_meta = meta_get(p.metas, name="robots")
    h1s = [t for lvl, t in p.headings if lvl == 1]
    visible_text = re.sub(r"<[^>]+>", " ", html)
    visible_text = re.sub(r"\s+", " ", visible_text).strip()
    word_count = len(visible_text.split())
    imgs_missing_alt = sum(1 for s, has, alt in p.images if not has or not alt.strip())
    og = {k: meta_get(p.metas, prop="og:" + k) for k in ("title", "description", "image", "type")}
    ld_types = []
    for raw in p.jsonld:
        for m in re.findall(r'"@type"\s*:\s*"([^"]+)"', raw):
            ld_types.append(m)
    # crude JS-rendering heuristic
    js_gated = word_count < 200 and p.script_count >= 3
    return {
        "url": url,
        "title": {"text": title, "length": len(title), "present": bool(title)},
        "meta_description": {"text": desc, "length": len(desc or ""), "present": bool(desc)},
        "meta_robots": robots_meta,
        "canonical": p.canonical,
        "html_lang": p.html_lang,
        "viewport": p.has_viewport,
        "h1_count": len(h1s),
        "h1": h1s,
        "headings": [{"level": l, "text": t} for l, t in p.headings],
        "question_headings": [t for l, t in p.headings if re.search(r"[?؟]\s*$", t) or
                              re.match(r"(?i)^(what|why|how|when|where|who|which|is|are|can|do|does|كيف|ما|لماذا|متى|أين|هل|من)\b", t)],
        "links_total": len(p.links),
        "open_graph": og,
        "images_total": len(p.images),
        "images_missing_alt": imgs_missing_alt,
        "jsonld_blocks": len(p.jsonld),
        "schema_types": sorted(set(ld_types)),
        "word_count_visible": word_count,
        "script_count": p.script_count,
        "js_rendering_suspected": js_gated,
    }


def analyze_robots(text):
    blocks, allowed, blocked = {}, [], []
    current_agents = []
    sitemaps = []
    for line in text.splitlines():
        s = line.split("#", 1)[0].strip()
        if not s:
            continue
        if ":" not in s:
            continue
        key, val = [x.strip() for x in s.split(":", 1)]
        kl = key.lower()
        if kl == "user-agent":
            current_agents = [val.lower()]
            blocks.setdefault(val.lower(), [])
        elif kl in ("allow", "disallow"):
            for ua in current_agents:
                blocks.setdefault(ua, []).append((kl, val))
        elif kl == "sitemap":
            sitemaps.append(val)
    crawler_status = {}
    for ua, (owner, purpose) in AI_CRAWLERS.items():
        rules = blocks.get(ua, [])
        disallow_root = any(k == "disallow" and v in ("/", "/*") for k, v in rules)
        status = "blocked" if disallow_root else ("explicit-allow" if rules else "default-allow")
        crawler_status[ua] = {"owner": owner, "purpose": purpose, "status": status}
    return {"sitemaps_listed": sitemaps, "ai_crawlers": crawler_status,
            "user_agents_seen": sorted(blocks.keys())}


def analyze_sitemap(text):
    locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", text, re.I)
    is_index = "<sitemapindex" in text.lower()
    lastmods = re.findall(r"<lastmod>\s*(.*?)\s*</lastmod>", text, re.I)
    return {"is_index": is_index, "url_count": len(locs),
            "sample": locs[:10], "has_lastmod": bool(lastmods)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html"); ap.add_argument("--url")
    ap.add_argument("--robots"); ap.add_argument("--sitemap"); ap.add_argument("--llms")
    ap.add_argument("--out")
    args = ap.parse_args()
    out = {}
    if args.html:
        with open(args.html, encoding="utf-8", errors="replace") as f:
            out["page"] = analyze_page(f.read(), args.url)
    if args.robots:
        with open(args.robots, encoding="utf-8", errors="replace") as f:
            out["robots"] = analyze_robots(f.read())
    if args.sitemap:
        with open(args.sitemap, encoding="utf-8", errors="replace") as f:
            out["sitemap"] = analyze_sitemap(f.read())
    if args.llms:
        with open(args.llms, encoding="utf-8", errors="replace") as f:
            t = f.read()
        out["llms_txt"] = {"present": True, "length": len(t),
                           "section_count": t.count("##")}
    else:
        out["llms_txt"] = {"present": False}
    js = json.dumps(out, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(js)
        print(f"wrote {args.out}")
    else:
        print(js)


if __name__ == "__main__":
    main()
