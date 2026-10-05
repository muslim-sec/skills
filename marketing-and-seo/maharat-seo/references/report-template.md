# Report Template — AUDIT-REPORT.md

Follow this structure exactly. Write in the user's language with English
keywords for technical terms; if language unspecified, write in English and add
the Arabic summary at the end. Fill every section with evidence from the actual
fetched pages — name the page/file behind each finding. Replace bracketed parts.

---

```markdown
# Maharat-SEO — SEO & AEO Audit: [domain]
*Audited [date] · prepared for an SEO/AEO expert handoff · by Maharat-SEO (Mahara AI)*

## 1. Executive summary
- **Overall Health Score: [XX]/100**
- **AI Search Readiness sub-score: [XX]/100**
- Business type detected: [type] · Market/audience: [..] · Target queries: [..]
- One-paragraph verdict: where the site stands and the single biggest lever.
- **Top 5 critical issues** (one line each, with priority tag).
- **Top 5 quick wins** (shippable this week).

## 2. Scorecard
| Category | Weight | Score | Notes |
|----------|-------|-------|-------|
| Technical SEO | 22% | [/100] | |
| Content & E-E-A-T | 22% | [/100] | |
| On-page SEO | 18% | [/100] | |
| AI Search Readiness (AEO/GEO) | 18% | [/100] | |
| Schema / structured data | 10% | [/100] | |
| Performance (CWV, best-effort) | 6% | [/100] | |
| Images & media | 4% | [/100] | |

## 3. Technical SEO findings
Crawlability, indexability, HTTPS/redirects, sitemap, robots.txt, rendering.
**Call out client-side-rendering explicitly if found.**

### AI crawler access
| Crawler | Allowed? | Surface |
|---------|----------|---------|
| OAI-SearchBot | | ChatGPT search |
| Googlebot | | Google + AIO |
| PerplexityBot | | Perplexity |
| ClaudeBot | | Claude |
| GPTBot | | training |
| Google-Extended | | Gemini training |
| CCBot | | training |
…explain what's blocked and the trade-off.

## 4. On-page SEO findings
Titles, meta, headings, URLs, internal links, OG/hreflang — with examples.

## 5. Content quality & E-E-A-T
Author/credentials/dates/sources/depth/duplication. Quote real examples.

## 6. Schema / structured data
What exists, what's broken, what's missing (with the right types for this business).

## 7. AI Search Readiness (AEO/GEO)
- Citability assessment (with quoted passages that work / don't).
- Structural readability.
- Technical accessibility (SSR, crawlers, schema, llms.txt — llms.txt low weight).
- Authority & brand signals off-site (Wikipedia/Reddit/YouTube/LinkedIn findings).
- Per-platform gaps (Google AIO / ChatGPT / Perplexity / Gemini / Bing).

## 8. Performance & images
Best-effort CWV risks + image issues. Recommend field data.

## 9. Ready-to-apply action plan
Grouped by priority. Each row is actionable.

### 🔴 Critical (now)
| # | Issue | Why it matters | Exact fix | Effort | Verify |
|---|-------|----------------|-----------|--------|--------|

### 🟠 High (~1 week)
| # | Issue | Why it matters | Exact fix | Effort | Verify |
|---|-------|----------------|-----------|--------|--------|

### 🟡 Medium (~1 month)
| # | Issue | Why it matters | Exact fix | Effort | Verify |
|---|-------|----------------|-----------|--------|--------|

### ⚪ Low (backlog)
| # | Issue | Why it matters | Exact fix | Effort | Verify |
|---|-------|----------------|-----------|--------|--------|

## 10. Quick wins (copy-paste ready)
- Ready `robots.txt` additions (if needed).
- Ready JSON-LD blocks (if needed).
- Ready `/llms.txt` (if absent) — built from the site's real sections.

## 11. Content rewrites for AI citability (before → after)
Pick 1–3 real passages. Show the current text, why it's hard to cite, and a
rewritten self-contained answer block (~130–170 words, direct answer up top).

## 12. Assumptions & limitations
Sample of pages audited, what was best-effort (e.g. performance without field
data), what needs tools/access to confirm (GSC, CrUX, DataForSEO).

---
## ملخص تنفيذي (Arabic summary — include only if the request language was unspecified)
- النتيجة الإجمالية: [XX]/100 · جاهزية البحث بالذكاء الاصطناعي: [XX]/100
- أهم 3 مشكلات حرجة: …
- أهم 3 مكاسب سريعة: …

*— Maharat-SEO · Mahara AI (maharaai.com) · Hossamudin.com*
```
