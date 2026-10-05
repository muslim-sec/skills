# AEO / GEO Criteria — AI Answer-Engine Readiness (2026)

> **Frame everything here as SEO fundamentals applied to AI-search surfaces.**
> Google's stated position is that optimizing for AI Overviews/SGE is still SEO;
> "AEO" and "GEO" are largely rebranded labels for the same work. When a popular
> AI-SEO tactic contradicts a primary source, defer to the primary source and
> note the contradiction in the report.

## Table of contents
1. Why AI visibility matters now
2. The five GEO levers (with scoring guidance)
3. Brand mentions vs backlinks
4. Platform-specific behavior
5. Myth-busting (what does NOT work)
6. Quick / medium / high-impact moves

---

## 1. Why it matters
AI answer engines (Google AI Overviews, ChatGPT search, Perplexity, Gemini,
Bing Copilot) now intercept a large and growing share of informational queries,
often answering without a click. Being *cited* in those answers is the new
visibility. The mechanics differ from blue-link ranking, so audit them
explicitly — but most fixes are good SEO regardless.

## 2. The five GEO levers

### Lever 1 — Citability (weight ~25% of AI sub-score)
AI engines extract self-contained passages. Reward:
- A direct answer in the **first 40–60 words** of a section.
- **Quotable passages ~130–170 words** that stand alone without surrounding context.
- Specific facts, numbers, dates — each ideally attributed to a source.
- Clean definitions: "X is …", "X refers to …".
- Unique data (original research, surveys) not found elsewhere.
Penalize: vague generalities, opinion without evidence, buried conclusions, no data.

### Lever 2 — Structural readability (weight ~20%)
Reward clean `H1→H2→H3`, **question-based headings** matching real queries,
short paragraphs (2–4 sentences), comparison **tables**, step **lists**, and
genuine **FAQ** Q&A blocks. Penalize walls of text, broken hierarchy, no lists/tables.

### Lever 3 — Technical accessibility (weight ~20%)
- **Server-side rendering is critical** — most AI crawlers do not run JavaScript.
  If main content is JS-only, it's effectively invisible to them.
- AI crawlers allowed in `robots.txt` (see `ai-crawlers.md`).
- Valid structured data.
- `llms.txt` present — **report it, but assign little/no citation weight** (see myths).

### Lever 4 — Authority & brand signals (weight ~20%)
Off-site signals matter more than people expect for AI citation:
- Presence in **Wikipedia / Wikidata**, **Reddit**, **YouTube**, **LinkedIn**.
- Third-party mentions of the brand and its key people.
- Author bylines with real credentials; `sameAs` entity linking.
Use `WebSearch` to check these — don't assume.

### Lever 5 — Platform fit (weight ~15%)
Optimize for where the gap is. Only a small minority of domains are cited by both
ChatGPT and Google AIO for the same query, so platform-specific work pays off.

## 3. Brand mentions vs backlinks
Industry studies (e.g. Ahrefs' large-scale 2025 analysis) find **brand mentions
correlate more strongly with AI visibility than backlink/Domain-Rating signals**.
YouTube and Reddit mentions show especially strong correlation. Treat
"earn mentions in the places AI engines trust" as a first-class recommendation,
not an afterthought. (Cite findings as correlational, not proven causation.)

## 4. Platform-specific behavior
| Platform | Leans on | Optimization focus |
|----------|----------|--------------------|
| Google AI Overviews | Top-ranking pages + passage quality | Classic SEO + passage/answer-block optimization |
| ChatGPT search | Wikipedia, authoritative sources | Entity presence, authoritative citations |
| Perplexity | Reddit, community + Wikipedia | Community validation, discussion presence |
| Gemini | Google index + entities | SEO + structured data + entity clarity |
| Bing Copilot | Bing index | Bing SEO, IndexNow submission |

## 5. Myth-busting — what does NOT (reliably) work
- **`llms.txt` as a ranking/citation lever** — major AI search systems are not
  documented to use it for citation selection; server-log studies find little
  evidence of it driving citations. Add it (harmless, future-friendly) but don't
  sell it as a ranking win.
- **Keyword-stuffed "AI rephrasing"** of pages to please models — not effective;
  reads as spam.
- **Mention-farming / fake citations** — Google explicitly rejects manufactured
  mentions as a tactic.
- **Mechanical "chunking" for chunk's sake** — structure should serve readers;
  there's no secret chunk size that games the model beyond genuinely clear, self-
  contained passages.
- **Schema as a magic citation switch** — schema aids understanding/eligibility;
  it is not a guaranteed citation lever, especially for purely commercial pages.

## 6. Impact tiers
**Quick wins:** add a 40–60 word "What is X?" answer up top; create 130–170 word
self-contained answer blocks; add question-based H2/H3; cite specific stats with
sources; add publish/updated dates; allow key AI crawlers; add Person schema for authors.

**Medium effort:** create `/llms.txt`; author bios with credentials + LinkedIn/Wikipedia
links; ensure SSR for key content; build presence on Reddit/YouTube; add comparison
tables; add real FAQ sections.

**High impact:** original research/surveys (unique citability); Wikipedia presence
for brand/key people; an active YouTube channel with mentions; comprehensive
entity linking (`sameAs` across platforms); proprietary tools/calculators.
