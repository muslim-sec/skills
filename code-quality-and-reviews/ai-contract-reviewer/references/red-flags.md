# Red Flag Catalog — What to Look For, by Contract Type

This is your scoring cheat sheet. For each contract type below, you'll find:
- **Clauses that always matter** (must score every one of these)
- **Market-standard ranges** (what a 1–2 looks like vs a 7–8)
- **Predatory patterns** (specific phrasings that should immediately trigger 8+)

Use this as a reference — don't paste it into the output. Use it to inform your scoring and to know when to push back.

---

## Universal red flags (apply to every contract)

These appear in almost every contract. Always score them.

### 1. Governing law & jurisdiction
- **Standard (1–2):** A reasonable jurisdiction where one of the parties is based, neutral courts.
- **Notable (5):** A jurisdiction where neither party is based and travel/legal costs would be punishing for the user.
- **Severe (8+):** A jurisdiction known for biasing toward one party type, or one with extremely slow/expensive enforcement, or a forum that effectively forecloses the user's ability to sue.

### 2. Dispute resolution / arbitration
- **Standard (1–3):** Mutual arbitration with a reputable body, or court litigation in a fair venue.
- **Notable (5–6):** Class-action waiver in a consumer-style contract; arbitration in a far-flung city.
- **Severe (8+):** Forced arbitration paid for entirely by the user; arbitrator selected solely by the other side; no right to discovery; clause designed to make claims uneconomical.

### 3. Termination
- **Standard (1–3):** Mutual termination for convenience with reasonable notice (typically 30–90 days); termination for cause with cure period.
- **Notable (5):** One-sided termination for convenience — only the other party can walk away.
- **Severe (8+):** User cannot terminate at all; long lock-in (3+ years) with massive early-termination penalties; termination clause that strips the user of work product or paid-but-unearned fees.

### 4. Payment terms
- **Standard (1–3):** Net 15 to Net 30; late fees of 1–1.5%/month.
- **Notable (5):** Net 60 or Net 90 — common in enterprise but rough on cash flow for a freelancer.
- **Severe (8+):** "Pay when paid" clauses tied to a third party; payment contingent on subjective "approval" with no objective standard; right to claw back paid fees after-the-fact for vague reasons.

### 5. Indemnification
- **Standard (1–3):** Mutual indemnity for third-party IP/breach claims, with reasonable carve-outs.
- **Notable (5–6):** One-sided indemnity but capped at fees paid or insurance limits.
- **Severe (8+):** Uncapped indemnity; user indemnifies the other side for the other side's own negligence; broad indemnity covering anything the other party "may incur" (including consequential / business-loss damages).

### 6. Limitation of liability
- **Standard (1–3):** Mutual cap at fees paid in the prior 12 months (vendor-side); consequential damages excluded mutually.
- **Notable (5):** Cap at a smaller amount (e.g., 1 month of fees) that wouldn't cover realistic damages.
- **Severe (8+):** One-sided cap — the user's liability is uncapped while the other side's is heavily capped. Cap so low it's a joke (e.g., "$100 total").

### 7. Confidentiality
- **Standard (1–3):** Mutual confidentiality; defined "Confidential Information"; standard 2–3 year tail; reasonable carve-outs (publicly known, independently developed, required by law).
- **Notable (5):** Asymmetric — user must protect everything, other side has wiggle room.
- **Severe (8+):** Perpetual confidentiality with no expiration; "Confidential Information" defined as everything the user ever sees including their own ideas; criminal-style penalties.

### 8. IP / work-product ownership
- This is **the** clause to scrutinize in any creative/technical contract.
- **Standard (1–3):** The party paying for specific deliverables owns those deliverables. The creator retains background IP and rights to general skills/methodologies.
- **Notable (5):** "Work for hire" assignment of *only* the commissioned work.
- **Severe (8+):** Assignment of *all* IP the user creates during the relationship (including unrelated personal projects); assignment of pre-existing IP; "moral rights" waivers; rights to user's name/likeness in perpetuity.

### 9. Non-compete / non-solicit
- **Standard (1–3):** Narrow non-solicit of named accounts for 6–12 months; no general non-compete.
- **Notable (5–6):** Broad non-compete limited to direct competitors, 12 months, in a defined geography.
- **Severe (8+):** Global non-compete; 2+ year duration; covers tangential industries; non-compete *and* non-solicit *and* non-disparagement stacked; non-competes that would be unenforceable in the user's jurisdiction (still worth flagging because the user shouldn't sign things designed to intimidate).

### 10. Assignment of contract
- **Standard (1–3):** Mutual consent required to assign.
- **Notable (5):** Other party can freely assign; user cannot.
- **Severe (7+):** Other party can assign to anyone including direct competitors of the user; combined with personal guarantee clauses.

### 11. Auto-renewal
- **Standard (1–3):** No auto-renewal, or auto-renew with short, easy cancellation window.
- **Notable (5):** Auto-renewal with 60–90 day notice window — easy to miss.
- **Severe (7+):** Auto-renewal with arbitrary unilateral price increases; auto-renewal where the cancellation must be by certified mail to a specific person; auto-renewal that compounds (1 year first, then 2 years, then 3).

### 12. Force majeure
- Mostly boilerplate. Score 1–3 unless egregious. **Severe (7+):** One-sided force majeure that excuses only the other party's performance; force majeure that survives indefinitely.

### 13. Modification / amendment
- **Standard (1–3):** Written mutual consent required.
- **Severe (7+):** One side can unilaterally modify terms with notice and continued use = consent.

### 14. Entire agreement / merger
- Mostly boilerplate. **Worth flagging (5)** if the user was promised something verbally that isn't in the written contract — that promise is now void.

---

## Contract-type specific patterns

### Employment contracts
Pay attention to: salary/comp structure, bonus discretion language, equity vesting (cliff, acceleration on change of control), non-compete enforceability in user's jurisdiction, IP assignment scope (does it grab personal projects?), arbitration with class-action waiver, severance, garden leave, "at-will" vs fixed-term, benefits clawback.

Common predatory pattern: "All IP you create during employment, on or off company time, using your own equipment or the company's, is assigned to the company." Score 8+. Push for a clear carve-out.

### Freelance / SOW / work-for-hire
Pay attention to: payment terms (especially milestone vs net-X), scope creep protection, change-order process, IP assignment (should only be for delivered work, not background IP), revisions cap, kill fees, late delivery penalties (often grossly disproportionate), client liability for content they provided.

Common predatory pattern: "Contractor assigns all rights including derivative works in perpetuity; Client may use Contractor's name, likeness, and portfolio rights without compensation." Score 8.

### NDA (Non-Disclosure)
Pay attention to: mutual vs one-way, definition of Confidential Information (breadth), term (2–5 years is standard; perpetual is suspect), residuals clause (often hidden, often important for the receiver), no-hire clauses snuck in, jurisdiction, injunctive relief language.

Common predatory pattern: One-way NDA presented as "standard" when the user is sharing material info; perpetual term; defining "Confidential Information" to include all information disclosed in any form ever. Score 7.

### SaaS / Vendor / Customer agreements
Pay attention to: SLA and remedies (service credits often laughable), data ownership and portability (who owns customer data, what happens on termination, export format), security and breach notification, auto-renewal, price escalation caps, audit rights, sub-processor approvals, data residency.

Common predatory pattern: "Provider may modify the service at its discretion; Customer's continued use constitutes acceptance; Customer has no right to refund for changes that diminish service." Score 7–8.

### Partnership / JV / co-founder agreements
Pay attention to: equity splits and vesting, IP contribution and ownership, decision rights (who decides what, voting thresholds), exit / buyout mechanism, drag-along / tag-along, deadlock resolution, capital call obligations.

Common predatory pattern: No vesting on founder equity (everyone owns their full stake from day one — disaster if anyone leaves). Score 8 just for the absence.

### Lease / Rental
Pay attention to: term and renewal terms, rent escalation, deposit conditions for return, who's responsible for repairs and at what threshold, subletting rights, early termination penalties, joint and several liability for co-tenants, what's included in rent (utilities, parking, maintenance fees), guarantor/cosigner obligations.

Common predatory pattern: Landlord retains deposit for "ordinary wear and tear" or has sole discretion over what constitutes damage. Score 7.

### Sales / Purchase (goods or services)
Pay attention to: warranty (express, implied, disclaimer scope), delivery terms (Incoterms if international), risk of loss transfer, inspection and rejection windows, payment terms, return / refund policy, limitations on warranty.

Common predatory pattern: "AS IS, WHERE IS, with all faults" plus "no representations of any kind" — fine for a used car flea-market deal, severe for a software platform or B2B supply.

### Loan / Financing
Pay attention to: interest rate (compare to local market), fees stack (origination, late, prepayment), default triggers (what counts as default, cross-default to other loans), acceleration, personal guarantees, collateral and security interest, prepayment rights and penalties, governing law.

Common predatory pattern: Acceleration on any default + cross-default to any other obligation + personal guarantee + broad collateral grant = score 9.

### Real Estate Purchase
Pay attention to: deposit / escrow terms, contingencies (financing, inspection, appraisal, title), title insurance, closing date and what happens on default, prorations, disclosures, "AS IS" clauses, easements and encumbrances, special assessments.

Always recommend a lawyer for real estate purchases regardless of overall score.

### Settlement / Release
Pay attention to: scope of release (what claims are released, including unknown claims), non-disparagement, confidentiality (often very broad), neutral references, payment timing and tax treatment, claw-back triggers (e.g., violations of NDA forfeit payment).

Often presented as "non-negotiable." It almost never is for material terms. Score the actual content, not the framing.

---

## Patterns that should always trigger 9 or 10

Regardless of contract type, if you see any of these, score the relevant clause 9 or 10:

1. **Personal guarantee** by an individual on a corporate contract that doesn't otherwise warrant one (e.g., a freelancer guaranteeing their LLC's obligations on a small SOW).
2. **Confession of judgment** clauses (waiving right to defend a future lawsuit).
3. **Waiver of jury trial AND class action AND right to attorney's fees** stacked together.
4. **Unilateral modification rights** combined with continued-use-equals-consent.
5. **Liquidated damages** that are clearly punitive rather than reasonable estimates of harm (e.g., "$10,000 per day of late delivery" on a $5,000 project).
6. **Assignment of unrelated IP** (employer claims rights to anything you create on personal time, on your own equipment, unrelated to their business).
7. **Indemnity for the other party's own gross negligence or intentional misconduct** — almost universally unenforceable but signals bad faith.
8. **No right to cure** before termination/default, combined with severe consequences.
9. **Perpetual non-compete** or non-compete with no geographic limit and no industry limit.
10. **Effective waiver of all damages** combined with limitation on remedies that leaves the user with no recourse for the other side's breach.

When you see one of these, your one-line verdict for that clause should be **"Walk away if they won't budge"** or its Arabic equivalent ("اطلب تعديلها أو انسحب").

---

## Things people miss that you should not

- **The defined-terms section.** Read it. Sneaky definitions of "Confidential Information," "Affiliate," "Services," "Deliverable," and "Change of Control" are how unfair contracts get written.
- **Cross-references.** "Subject to Section 12.3" — go read 12.3. The actual obligation is often nested two layers deep.
- **Schedules, exhibits, and addenda.** They have the same legal force as the main document. If they're referenced but not attached, flag it.
- **Notice provisions.** How does each party send legal notice? If it's certified mail to a specific person in a specific country, that's a way to make termination practically impossible for the user.
- **Severability.** Boring but matters — if a court strikes one clause, does the rest survive? Usually yes; flag if no.
- **Survival clauses.** Which obligations outlive the contract's termination? Often the bad ones (indemnity, confidentiality, non-compete) survive while the good ones (payment, performance) don't.

---

## What "market standard" actually means

When you score, anchor yourself to what a fair version of this clause looks like in the user's industry and jurisdiction. If you genuinely don't know, say so in your reasoning rather than guess — and round toward "ask a lawyer" for the action point.

Don't penalize a contract for being formal or long. Penalize it for being **one-sided, hidden, or abusive**. A 50-page enterprise SaaS agreement can be totally fair; a 1-page freelance gig can be a trap.
