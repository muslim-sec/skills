---
name: best-price-finder
description: Hunt the best online and offline price for a product (from a product name OR an attached image) across 10-20+ stores in the user's country, filter to in-stock only, convert to local currency, and present a comparison table with links plus recommendations. ALWAYS use this skill whenever the user asks about prices, where to buy, "best deal", "cheapest", "كم سعر", "أحسن سعر", "أرخص مكان", "where can I get", "price check", "compare prices", or attaches a product photo and asks about it — even if they don't explicitly say "find me the best price". Triggers on phrases like "I want to buy X", "looking for X", "how much is X here", and product photos with any buying/pricing intent. Trigger generously — it's better to over-trigger than miss a price-hunt request.
---

# Best Price Finder

Help the user find the best price for a product — both online and offline — within their country, filtered to what's actually in stock, presented in their currency.

## When this triggers
The user wants to buy something and is comparing prices, OR they want to know where to buy a product, OR they sent a product image and asked about it. The product may come as:
- A name/model (e.g., "Sony WH-1000XM5", "iPhone 15 Pro 256GB", "Dyson V11")
- An attached image
- A vague description ("that black gaming chair from the ad")

## Core workflow

### Step 1 — Identify the product
If the user sent an image, identify the product as specifically as possible: brand, model, capacity/size/color variant. State your read of it back to the user in one line and proceed; only stop to ask if the image is too ambiguous to search confidently. If they sent a name, normalize it to a searchable form (full brand + model + key variant — e.g., "iPhone 15 Pro 256GB Natural Titanium" not just "iPhone").

### Step 2 — Lock down location and language
Country and language drive which stores to search and which currency to quote. Resolve them in this order:

1. **Memory / context first** — check `CLAUDE.md` or session memory for the user's country and city. If stored, use it without asking.
2. **Conversation clues** — if the user mentioned a city, used a local dialect, or referenced local stores in this conversation, infer from that.
3. **Default to Egypt (EGP)** if there's nothing to go on, but ask one quick confirming question before searching: "Searching in Egypt — confirm or tell me a different country?"
4. **City prompt** — only ask for city when offline/in-store availability matters (electronics, big-ticket items, anything where pickup or showroom visits are common). For commodity online-only purchases, country is enough.

**Output language**: match the language of the user's most recent message. If they wrote in Arabic, respond entirely in Arabic (table headers, recommendations, store names where conventional). If English, English. If mixed, match the dominant language of their request.

### Step 3 — Search broadly across 10-20+ stores
Cast a wide net. The store list depends on country — see `references/stores-egypt.md`, `references/stores-saudi.md`, `references/stores-uae.md` for curated lists by category. For other countries, build your own list using these categories:

- **Mega-marketplaces** (Amazon local domain, Noon, Jumia, eBay where relevant)
- **Category specialists** (electronics: B.TECH, Jarir, Sharaf DG, Extra; fashion: Namshi, SHEIN MENA; home: IKEA local, Home Centre)
- **Brand official websites** (Apple.com/eg, Samsung.com/eg, Sony, etc.)
- **Authorized resellers and chains** (ElAraby Group, 2B, Tradeline, Compumarts, Saco)
- **Physical big-box / hypermarkets with online presence** (Carrefour, Lulu, Spinneys, HyperOne, HyperPanda)
- **Local price comparison aggregators** (Yaoota in Egypt is a strong signal)

Use web search with site-targeted queries when needed (e.g., `site:noon.com "Sony WH-1000XM5"`) to dig past noisy SERPs. Run searches in parallel — don't go store-by-store sequentially when you can fan out.

### Step 4 — Filter to in-stock only
This is non-negotiable: a price on an out-of-stock listing is worthless to the buyer. For each candidate listing:
- Confirm the page shows "In Stock", "Available", "Add to Cart" enabled, "متاح", "متوفر" — NOT "Out of Stock", "Notify me", "غير متوفر", "نفذ من المخزون".
- If you can't tell from search snippets alone, fetch the page to check.
- **Skip out-of-stock listings entirely.** Don't list them with a strikethrough or footnote — they create noise. Just drop them.
- Note delivery time/availability briefly if it's unusual (e.g., "3-week wait" or "ships from abroad").

### Step 5 — Normalize prices to local currency
Quote every price in the user's local currency, formatted naturally for that locale (EGP 24,500 / 24,500 ج.م / SAR 1,899 / AED 1,599). If a store lists in USD or another foreign currency, convert at current rate and note it in parentheses: "EGP 22,400 (~$450)". Be transparent about VAT — note if a store's price excludes VAT.

### Step 6 — Build the comparison table
**Always end with a table.** Columns:

| Store | Type | Price | Stock | Delivery | Link |
|---|---|---|---|---|---|

- **Type** = Online / Offline / Both (offline only if there's a physical store presence the user can visit; mark "Both" when the retailer has both)
- **Stock** = In Stock (confirmed) — and if there's any nuance, say "Limited" or "Pre-order"
- **Delivery** = same-day / 2-3 days / 1 week / pickup available
- **Link** = direct product page, not the store homepage

Sort by price ascending. Include 5-10 rows in the table — the best of what you found, not all 20+ stores you checked.

### Step 7 — Recommendations
After the table, give 2-4 sentences of opinionated guidance — not just a recap. Examples of what good recommendations look like:

- "Cheapest legit option is **Noon at EGP 22,400** with 2-day delivery. **B.TECH at EGP 23,100** is barely more and worth it if you want a physical receipt and easy in-person warranty claims."
- "Skip the EGP 19,900 listing on Jumia — that seller has a 2.1★ rating and the product page is missing the official warranty info. The next cheapest verified one is Amazon.eg at EGP 22,800."
- "Best value is **Jarir at SAR 1,899** with free delivery. If you can wait until Jarir's monthly sale (usually first week), it sometimes drops to SAR 1,749."

Call out: best overall, best for fast delivery, best for in-store pickup (if relevant), and any traps to avoid (suspicious sellers, fake-looking listings, refurb sold as new).

### Step 8 — Alternatives — only when warranted
**Don't reflexively offer alternatives every time.** Only offer them when:
- The product is **out of stock everywhere** you searched
- The lowest verified price is **clearly overpriced** vs. what the user might expect (e.g., a known model selling at 30%+ above MSRP, or where a better-value newer model exists for similar money)
- The user explicitly asked

When you do offer, phrase it as a follow-up: "Want me to look at alternatives? The [Model X] is similar at a lower price, or [Model Y] is the newer version for slightly more." Then wait for them to say yes before doing the second search.

## Output structure

Always structure the response in this order:
1. **One-line confirmation** of what you searched for and where ("Searching for *Sony WH-1000XM5 black* in Egypt across 18 stores…" — keep this short, it sets expectations)
2. **Comparison table** (sorted by price ascending)
3. **Recommendations** (2-4 sentences, opinionated, names the winner)
4. **Alternatives offer** (only if warranted per Step 8)

## Things to be careful about

**Sketchy listings** — A price 40% below everyone else is usually a scam, a typo, an unboxed/damaged unit, or a different variant (smaller capacity, gray import, refurb). Cross-check before recommending it. If unsure, list it but flag it: "Note: this listing is unusually low — verify it's the same variant before ordering."

**Gray market vs. official** — In MENA especially, parallel imports often undercut official channels but lack local warranty. Mention this distinction when relevant ("this seller is a parallel importer — no Samsung Egypt warranty, only seller warranty").

**Price freshness** — Prices change. If you fetched a price and it doesn't match what the user sees on the page when they click through, that's normal. Don't promise prices, present them as "as of [today's date]".

**Don't pad the table** — If only 6 stores have it in stock, the table has 6 rows. Don't pad with out-of-stock entries to hit 10.

**Bilingual store names** — In Arabic responses, use the store's commonly-used Arabic name when one exists (نون, جوميا, بي تك), but keep the link as-is.
