# Classic SEO Criteria — what to test and how to judge it

Use this as the checklist behind the Technical / On-page / Content / Schema /
Performance / Images categories. For each item, record evidence (the page or
file you saw it on) so scores are defensible.

## Technical SEO
- **HTTPS** everywhere; no mixed content; valid certificate.
- **Canonicalization**: http→https and www/non-www resolve to one version; no
  redirect chains/loops (≤1 hop ideal).
- **robots.txt**: present, not accidentally blocking important paths; lists
  sitemap. Check AI crawlers separately (see `ai-crawlers.md`).
- **XML sitemap**: present, referenced in robots.txt, only canonical 200 URLs,
  reasonably fresh, submitted to Search Console (note if unknown).
- **Indexability**: key pages not `noindex`; pagination/filters handled; no
  important content behind login or JS-only rendering.
- **Status codes**: money/content pages return 200; broken internal links flagged.
- **Mobile**: responsive viewport meta; no horizontal scroll; tap targets.
- **Security headers** (best-effort): HSTS, X-Content-Type-Options, etc.

## On-page SEO
- **Title tag**: unique, ~50–60 chars, primary intent/keyword near front, brandable.
- **Meta description**: unique, ~140–160 chars, compelling, intent-matched (note:
  not a ranking factor but drives CTR and is often used by AI snippets).
- **Headings**: exactly one `<h1>`; logical `H2/H3`; descriptive, ideally
  question-shaped where it matches search intent.
- **URL**: readable, lowercase, hyphenated, not over-parameterized.
- **Internal linking**: important pages linked from nav/body with descriptive
  anchor text; no orphan pages; reasonable depth from homepage.
- **Open Graph / Twitter cards** for share/preview correctness.
- **hreflang** for multilingual/multiregional sites (correct return tags).

## Content quality & E-E-A-T
- **Experience/Expertise/Authoritativeness/Trust**: author bylines + credentials,
  about/contact, real organization info, citations to primary sources.
- **Freshness**: visible publish + last-updated dates where relevant.
- **Depth vs thin**: does the page actually satisfy the query, or is it thin/
  templated/duplicated? Flag near-duplicate or boilerplate pages.
- **Intent match**: does page type fit query type (informational vs commercial
  vs transactional)?
- **Keyword targeting**: covered naturally; not stuffed; semantically complete
  (related entities/subtopics present).

## Schema / structured data
- Detect JSON-LD (preferred) / microdata. Map to the right types per business:
  - Any site: `Organization`, `WebSite` (+ Sitelinks Searchbox), `BreadcrumbList`.
  - Publisher/blog: `Article`/`BlogPosting` + `Person` author.
  - E-commerce: `Product` + `Offer` + `AggregateRating`/`Review`.
  - Local: `LocalBusiness` (+ correct `@type`), `geo`, `openingHours`.
  - How-to/FAQ: `FAQPage`/`HowTo` (note Google's reduced FAQ rich-result
    eligibility — still useful for understanding, not guaranteed rich result).
- Flag validation issues (missing required props, wrong nesting) and high-value
  missing schema. Provide paste-ready JSON-LD in the report.

## Performance (Core Web Vitals — best-effort lab signal)
- **LCP** risk: large hero images, render-blocking CSS/JS, slow TTFB.
- **CLS** risk: images without dimensions, injected banners.
- **INP** risk: heavy JS, long tasks, many third-party scripts.
- Page weight, number of requests, third-party script count.
- State clearly this is a lab estimate; recommend **field data** (CrUX /
  PageSpeed Insights / Search Console) for ground truth.

## Images & media
- `alt` text coverage (descriptive, not stuffed).
- Modern formats (WebP/AVIF), correct sizing, lazy-loading below the fold.
- Descriptive filenames; image sitemap if media-heavy.

## Local SEO (only when business is local/brick-and-mortar)
- NAP (Name/Address/Phone) consistency across site + listings.
- Google Business Profile presence (note if checkable), reviews, `LocalBusiness`
  schema, embedded map, location/service-area pages.
