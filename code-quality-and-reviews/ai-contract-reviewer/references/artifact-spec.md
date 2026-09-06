# Artifact Specification

This is the data model and visual spec for the HTML output. Read this before you build the artifact so you know what fields and structure are expected.

## Data shape

Before you render, organize the review into this structure (you can keep it in your head or briefly write it out; you don't have to emit JSON):

```
{
  "meta": {
    "contract_type": "Freelance / SOW",
    "language": "ar" | "en",
    "parties": ["Acme Inc.", "Jane Doe"],
    "user_role": "Contractor",
    "governing_law": "Saudi Arabia",
    "effective_date": "2026-06-01",
    "term": "12 months",
    "review_date": "2026-05-16"
  },
  "verdict": {
    "traffic_light": "amber",      // green | amber | orange | red
    "overall_score": 6.5,           // 1.0 – 10.0
    "headline": "Sign with edits — negotiate IP and payment first",
    "summary": "Two short paragraphs explaining why."
  },
  "top_issues": [
    {"label": "...", "score": 8, "clause_id": "c12"},
    ...
  ],
  "clauses": [
    {
      "id": "c1",
      "label": "Termination for convenience",
      "score": 4,
      "verdict": "Acceptable, but worth knowing",
      "reasoning": "Both parties can terminate with 30 days...",
      "redline": "Optional — what alternate text to propose, or null for low scores",
      "quote": "Either party may terminate this Agreement..."  // exact text in contract
    },
    ...
  ],
  "actions": [
    {
      "priority": "must-do",       // must-do | should-do | nice-to-do
      "title": "Negotiate IP carve-out",
      "detail": "Push for explicit exclusion of pre-existing work and personal projects.",
      "related_clauses": ["c7"]
    }
  ]
}
```

## Color palette

| Score | Color (light) | Color (dark) | Use |
|---|---|---|---|
| 1–2 | `#dcfce7` bg / `#166534` text | `#14532d` bg / `#bbf7d0` text | Green — fine |
| 3–4 | `#ecfccb` bg / `#3f6212` text | `#365314` bg / `#d9f99d` text | Yellow-green — minor |
| 5 | `#fef9c3` bg / `#854d0e` text | `#713f12` bg / `#fef08a` text | Yellow — notable |
| 6–7 | `#fed7aa` bg / `#9a3412` text | `#7c2d12` bg / `#fed7aa` text | Orange — serious |
| 8–9 | `#fecaca` bg / `#991b1b` text | `#7f1d1d` bg / `#fecaca` text | Red — severe |
| 10 | `#fca5a5` bg / `#7f1d1d` text | `#450a0a` bg / `#fca5a5` text | Dark red — deal-breaker |

Use these as the background for the highlight `<mark>` elements and the score badges.

## Visual hierarchy

1. **Hero verdict** (above the fold): traffic light circle (large, prominent), one-line headline, overall score, sign-or-don't recommendation. Designed so the user makes a decision in the first 5 seconds.

2. **Risk dashboard** (below verdict): 
   - Top 5 issues as cards (clickable, jump to the clause)
   - Distribution bar: 10 segments, one per score, showing how many clauses fell in each
   - Contract metadata: type, parties, governing law, term, review date

3. **Contract body**: the full text, with every scored clause wrapped in a colored `<mark>` element. The label and score appear in a small badge next to the highlight on desktop, or above it on mobile. Clicking the highlight either:
   - On desktop: opens a sliding side panel from the right (left for RTL) showing label, score badge, verdict, reasoning, redline.
   - On mobile: expands inline, pushing the rest of the text down, with a "Close" button.

4. **Action points**: ordered list. Each item:
   - Checkbox (visual only — the user can tick it but it's not persisted)
   - Priority badge (must-do / should-do / nice-to-do)
   - One-sentence what-to-do
   - Small "see clause" link that jumps to the related clause(s)

5. **Footer**: legal disclaimer ("This is AI-assisted review and not legal advice. For high-stakes or jurisdiction-specific questions, consult a licensed attorney."), generation date, "Re-review" reminder.

## Interactions

- **Language toggle** in the header (only show if contract is bilingual or user explicitly asked for both): swap all UI strings and flip `dir` on the root.
- **Print stylesheet**: action points and dashboard should print on the first page; contract body on subsequent pages with highlights preserved as colored backgrounds. Hide the interactive side-panel UI.
- **Jump-to-clause**: clicking a top-issue card or an action-point's "see clause" link smooth-scrolls the contract body to the clause and pulses the highlight briefly.
- **Anonymization**: an optional toggle in the header replaces party names with "Party A" / "Party B" so the user can share the artifact externally without leaking names. Implement by storing the original names and the placeholder versions, swapping in the DOM on click.

## Hard requirements

- **Single file** — everything inline. No CDN. No fetch calls. No `localStorage`. Should work emailed to anyone, opened from a USB drive, anywhere.
- **Mobile-friendly** — works on a 360px-wide phone. The side panel becomes an inline expansion. The dashboard cards stack.
- **Accessible** — semantic HTML, ARIA labels on the interactive elements, keyboard navigable. The contract body should be selectable / copyable.
- **RTL support** — every layout choice that uses left/right padding/margin must use logical properties so it flips correctly when `dir="rtl"` is set on `<html>`.
- **Lightweight** — under ~300KB. No frameworks. Vanilla JS only. The user's browser should open it instantly.

## Things to NOT do

- Don't use frameworks (no React, no Vue) — vanilla JS only.
- Don't use a CDN for fonts or anything else — system fonts are fine and faster.
- Don't include the entire `red-flags.md` or `scoring-rubric.md` content in the artifact — only the per-clause review.
- Don't make the user log in or set up anything. The artifact is fire-and-forget.
- Don't try to make it editable. The user can't edit clause scores in the artifact. If they disagree, they go back to chat.
