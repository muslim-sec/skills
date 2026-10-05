#!/usr/bin/env python3
"""
Maharat-SEO — interactive dashboard generator.

Turns a findings JSON into a single self-contained, themeable HTML file
(no external assets except Chart.js from CDN). Works for LTR and RTL (Arabic).

Usage:
  python3 build_dashboard.py findings.json --out dashboard.html [--rtl]

Expected findings JSON shape (produce this from your audit):
{
  "domain": "example.com",
  "date": "2026-05-30",
  "lang": "en",                # or "ar"; --rtl flag also forces RTL
  "overall_score": 72,
  "ai_score": 58,
  "business_type": "SaaS",
  "summary": "One-paragraph verdict.",
  "categories": [
    {"name": "Technical SEO", "weight": 22, "score": 80, "note": "..."},
    ...
  ],
  "ai_crawlers": [
    {"crawler": "OAI-SearchBot", "status": "blocked", "surface": "ChatGPT search"},
    ...
  ],
  "actions": [
    {"priority": "Critical", "issue": "...", "why": "...",
     "fix": "...", "effort": "S", "verify": "..."},
    ...
  ]
}
Priorities must be one of: Critical, High, Medium, Low.
"""
import argparse, json, html as _h

PRIO_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
PRIO_COLOR = {"Critical": "#e5484d", "High": "#f76808",
              "Medium": "#ffb224", "Low": "#8b8d98"}


def esc(s):
    return _h.escape(str(s if s is not None else ""))


def score_color(v):
    return "#30a46c" if v >= 80 else "#ffb224" if v >= 60 else "#e5484d"


def build(d, rtl=False):
    rtl = rtl or d.get("lang") == "ar"
    dir_attr = "rtl" if rtl else "ltr"
    cats = d.get("categories", [])
    crawlers = d.get("ai_crawlers", [])
    actions = sorted(d.get("actions", []),
                     key=lambda a: PRIO_ORDER.get(a.get("priority"), 9))
    cat_labels = json.dumps([c["name"] for c in cats], ensure_ascii=False)
    cat_scores = json.dumps([c.get("score", 0) for c in cats])
    cat_colors = json.dumps([score_color(c.get("score", 0)) for c in cats])

    cat_rows = "".join(
        f'<tr><td>{esc(c["name"])}</td><td>{esc(c.get("weight",""))}%</td>'
        f'<td><b style="color:{score_color(c.get("score",0))}">{esc(c.get("score",0))}</b>/100</td>'
        f'<td>{esc(c.get("note",""))}</td></tr>' for c in cats)

    crawl_rows = "".join(
        f'<tr><td>{esc(c["crawler"])}</td>'
        f'<td><span class="pill {("bad" if c.get("status")=="blocked" else "good")}">{esc(c.get("status"))}</span></td>'
        f'<td>{esc(c.get("surface",""))}</td></tr>' for c in crawlers)

    action_cards = "".join(
        f'<div class="action" data-prio="{esc(a.get("priority"))}">'
        f'<div class="action-h"><span class="badge" style="background:{PRIO_COLOR.get(a.get("priority"),"#888")}">{esc(a.get("priority"))}</span>'
        f'<span class="eff">effort: {esc(a.get("effort",""))}</span></div>'
        f'<div class="issue">{esc(a.get("issue"))}</div>'
        f'<div class="why"><b>Why:</b> {esc(a.get("why"))}</div>'
        f'<div class="fix"><b>Fix:</b> {esc(a.get("fix"))}</div>'
        f'<div class="verify"><b>Verify:</b> {esc(a.get("verify"))}</div>'
        f'</div>' for a in actions)

    return f"""<!doctype html>
<html lang="{esc(d.get('lang','en'))}" dir="{dir_attr}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maharat-SEO — {esc(d.get('domain'))}</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{{--bg:#0f1115;--card:#171a21;--ink:#e7e9ee;--mut:#9aa0ab;--line:#262b35;--accent:#6e8bff;}}
@media(prefers-color-scheme:light){{:root{{--bg:#f6f7f9;--card:#fff;--ink:#1a1d24;--mut:#5b616e;--line:#e6e8ec;}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.55 -apple-system,Segoe UI,Roboto,'Noto Sans Arabic',sans-serif;padding:28px;}}
.wrap{{max-width:1040px;margin:0 auto}}h1{{font-size:22px;margin:0 0 2px}}
.sub{{color:var(--mut);margin-bottom:22px}}
.grid{{display:grid;gap:16px}}.g2{{grid-template-columns:1fr 1fr}}.g3{{grid-template-columns:repeat(3,1fr)}}
@media(max-width:760px){{.g2,.g3{{grid-template-columns:1fr}}}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px}}
.gauge{{text-align:center}}.gauge .n{{font-size:42px;font-weight:800;line-height:1}}
.gauge .l{{color:var(--mut);font-size:13px;margin-top:4px}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{text-align:start;padding:8px 6px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{color:var(--mut);font-weight:600}}
.pill{{padding:2px 9px;border-radius:20px;font-size:12px;font-weight:600}}
.pill.good{{background:rgba(48,163,108,.15);color:#30a46c}}.pill.bad{{background:rgba(229,72,77,.15);color:#e5484d}}
h2{{font-size:16px;margin:26px 0 12px}}
.filters{{margin:8px 0 14px;display:flex;gap:8px;flex-wrap:wrap}}
.filters button{{background:var(--card);border:1px solid var(--line);color:var(--ink);
padding:6px 14px;border-radius:20px;cursor:pointer;font-size:13px}}
.filters button.on{{border-color:var(--accent);color:var(--accent)}}
.action{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}}
.action-h{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}
.badge{{color:#fff;padding:2px 10px;border-radius:6px;font-size:12px;font-weight:700}}
.eff{{color:var(--mut);font-size:12px}}.issue{{font-weight:700;margin-bottom:6px}}
.why,.fix,.verify{{font-size:13.5px;color:var(--ink);margin-top:4px}}
.why b,.fix b,.verify b{{color:var(--mut)}}
.foot{{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}}
.foot a{{color:var(--accent);text-decoration:none}}
</style></head>
<body><div class="wrap">
<h1>Maharat-SEO — {esc(d.get('domain'))}</h1>
<div class="sub">{esc(d.get('business_type',''))} · {esc(d.get('date',''))} · SEO &amp; AEO audit</div>

<div class="grid g3">
  <div class="card gauge"><div class="n" style="color:{score_color(d.get('overall_score',0))}">{esc(d.get('overall_score',0))}</div><div class="l">Overall Health /100</div></div>
  <div class="card gauge"><div class="n" style="color:{score_color(d.get('ai_score',0))}">{esc(d.get('ai_score',0))}</div><div class="l">AI Search Readiness /100</div></div>
  <div class="card"><canvas id="catChart" height="150"></canvas></div>
</div>

<div class="card" style="margin-top:16px">{esc(d.get('summary',''))}</div>

<h2>Category scores</h2>
<div class="card"><table><thead><tr><th>Category</th><th>Weight</th><th>Score</th><th>Notes</th></tr></thead><tbody>{cat_rows}</tbody></table></div>

<h2>AI crawler access</h2>
<div class="card"><table><thead><tr><th>Crawler</th><th>Status</th><th>Surface</th></tr></thead><tbody>{crawl_rows}</tbody></table></div>

<h2>Action plan</h2>
<div class="filters">
  <button class="on" data-f="all">All</button>
  <button data-f="Critical">Critical</button>
  <button data-f="High">High</button>
  <button data-f="Medium">Medium</button>
  <button data-f="Low">Low</button>
</div>
<div id="actions">{action_cards}</div>

<div class="foot">Generated by <b>Maharat-SEO</b> · Created by the team at
<a href="https://www.maharaai.com/ar">Mahara AI</a> · Hossamudin.com</div>
</div>
<script>
new Chart(document.getElementById('catChart'),{{
 type:'bar',
 data:{{labels:{cat_labels},datasets:[{{data:{cat_scores},backgroundColor:{cat_colors},borderRadius:6}}]}},
 options:{{indexAxis:'y',plugins:{{legend:{{display:false}}}},
   scales:{{x:{{max:100,grid:{{color:'rgba(128,128,128,.15)'}}}},y:{{grid:{{display:false}}}}}}}}
}});
const btns=document.querySelectorAll('.filters button');
btns.forEach(b=>b.onclick=()=>{{
 btns.forEach(x=>x.classList.remove('on'));b.classList.add('on');
 const f=b.dataset.f;
 document.querySelectorAll('.action').forEach(a=>{{
   a.style.display=(f==='all'||a.dataset.prio===f)?'block':'none';}});
}});
</script>
</body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("findings")
    ap.add_argument("--out", default="dashboard.html")
    ap.add_argument("--rtl", action="store_true")
    args = ap.parse_args()
    with open(args.findings, encoding="utf-8") as f:
        d = json.load(f)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(build(d, rtl=args.rtl))
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
