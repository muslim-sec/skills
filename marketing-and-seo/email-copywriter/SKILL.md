---
name: email-copywriter
description: Use when the user needs to write, draft, or compose any type of email including cold outreach, follow-ups, client updates, formal business, apologies, introductions, or internal team communications
---

# Email Copywriter

Professional email writing skill. Produces short, high-impact emails that sound human, not AI-generated.

**REQUIRED SUB-SKILL:** Every email draft MUST be processed through the `humanizer` skill (embedded mode) before delivery. No exceptions.

## Iron Rule

Do NOT write the email immediately. You MUST complete the intake grill first. Writing before the grill is finished is a violation.

## When NOT to Use

- Automated transactional emails (password resets, receipts). Those need templates, not copywriting.
- Legal or compliance emails. Those need a lawyer, not a copywriter.
- Mass marketing newsletters. Use a dedicated email marketing skill instead.

## Adaptive Intake Grill

Before writing, you need answers to these questions. If the user's initial message already answers some, skip those and ask only what is missing. Never ask a question the user already answered.

### Required Context (ask what is missing)

| Question | Why it matters |
|----------|---------------|
| Who is the recipient? (role, company) | Determines formality and jargon level |
| Do they know you, or is this first contact? | Cold vs. warm changes everything |
| Is their position higher, equal, or lower? | Calibrates deference vs. directness |
| What do you want? (pitch, ask, follow-up, apology, update, intro, thank-you, negotiation, resignation, complaint, invitation) | Selects the email framework |
| What tone? (formal / polite-warm / casual / confident-persuasive / direct-minimal) | If not specified, infer from context and confirm |
| How short? (3-5 lines / 6-8 lines / medium) | Default to shortest viable length |
| Language? (English, Arabic, other) | Affects greeting conventions and structure |
| Anything to avoid? (words, topics, cultural sensitivities) | Only ask if context suggests sensitivity |
| Key points that MUST appear? | Only ask if purpose is complex |
| Previous context? (prior emails, what happened) | Only ask for follow-ups or threads |
| What should the reader DO after reading? | The single most important question for any email |

**Grill completion rule:** You have enough when you know WHO, WHY, TONE, and the DESIRED ACTION. Everything else is refinement.

## Email Type Classification

After the grill, silently classify into one of these types. Use the classification to select the structure and framework. Do not announce the classification to the user.

### Cold Email
**Structure:** Hook (1 line) + Credibility or relevance (1 line) + Ask (1 line) + Sign-off
**Framework:** Use PAS (Problem-Agitate-Solve) or direct value proposition
**Rules:**
- Maximum 4-5 sentences total
- First line MUST reference something specific about the recipient (their work, company, a recent post). Generic cold emails get deleted.
- One ask only. "Would you be open to a 15-min call?" not "Let me know your thoughts and also here is my portfolio and also I have three packages."
- Include a P.S. line with a soft second hook (a link, a relevant stat, a mutual connection)

### Follow-Up Email
**Structure:** Callback to original (1 line) + New angle or added value (1 line) + Easy exit (1 line)
**Rules:**
- Shorter than the original
- No blame, no guilt, no "just checking in"
- Add new value: a resource, an insight, a reason to respond now
- Provide an explicit exit: "If the timing isn't right, no worries at all."
- Follow-up #1: 3-5 days after original. Follow-up #2: 7-10 days. Follow-up #3 (final): 14 days with a breakup line.

### Business Formal
**Structure:** Purpose (1 line) + Context/details (2-3 lines) + Action required (1 line) + Closing
**Rules:**
- No contractions, no humor, no personality quirks
- Every sentence serves a function
- Clean paragraph breaks between sections

### Business Casual
**Structure:** Warm opener (1 line, not a cliche) + Body (flexible) + Next step + Friendly close
**Rules:**
- Contractions allowed, light personality allowed
- Most common email type. Default to this when unsure.

### Internal / Team Email
**Structure:** What + Why + Action items with owners and deadlines
**Rules:**
- Skip pleasantries beyond one line
- Bullet points for action items
- Bold the deadline if there is one

### Client Communication
**Structure:** Status/update + What it means for them + Next step from your side + What you need from them (if anything)
**Rules:**
- No jargon unless the client uses it first
- Reassuring and confident
- End with what happens next, not a vague sign-off

### Apology / Correction
**Structure:** Acknowledge the problem (1 line) + What caused it (1 line, no excuses) + What you are doing to fix it (1-2 lines) + What you are doing to prevent it
**Rules:**
- One apology. Not three.
- No defensive language ("Unfortunately, due to circumstances beyond our control...")
- Own it, fix it, move on.

### Introduction / Referral
**Structure:** Who you are introducing + Why they should talk + One line of context per person + Explicit next step
**Rules:**
- Keep it under 5 sentences
- Make it easy for both sides to reply

## Persuasion Frameworks

Select the right framework based on the email's purpose:

**PAS (Problem-Agitate-Solve):** Best for cold emails and pitches.
- State a problem the recipient has
- Make them feel the cost of not solving it
- Present your solution

**AIDA (Attention-Interest-Desire-Action):** Best for longer persuasive emails.
- Hook their attention (first line)
- Build interest with a relevant detail
- Create desire with a benefit or proof point
- Call to action

**BAB (Before-After-Bridge):** Best for case-study-style pitches.
- Describe their current state (before)
- Describe the improved state (after)
- Bridge: how you get them there

**Direct Ask:** Best for internal, team, and simple requests.
- State what you need
- State why
- State the deadline

## Subject Line Methodology

Write the subject line LAST, after the email body is done.

**Patterns that work:**

| Pattern | Example |
|---------|---------|
| Specific + short | "Pentesting proposal for Acme" |
| Question | "Quick question about your API security" |
| Mutual connection | "Sarah Chen suggested I reach out" |
| Relevant trigger | "Saw your talk at DEF CON" |
| Direct benefit | "Cut your CI pipeline time by 40%" |

**Rules:**
- Under 7 words when possible
- No ALL CAPS, no clickbait, no emojis
- Specific beats clever. "Meeting follow-up: next steps" beats "Touching base!"
- For follow-ups: "Re: [original subject]" or add "(follow-up)" to the original

## P.S. Lines

The P.S. is one of the most-read parts of any email. Use it strategically in cold and pitch emails:

- Link to a relevant resource, case study, or portfolio piece
- Drop a specific stat or result
- Mention a mutual connection
- Add a time-bound element ("I'll be in Dubai next week if an in-person coffee works better")

Do NOT use P.S. in formal, internal, or apology emails.

## Writing Rules

These rules apply to every email:

1. **Sound human.** Varied rhythm, natural phrasing, contractions when tone permits.
2. **Strong first line.** The opener must earn the next sentence. See Banned Openings below.
3. **Every sentence earns its place.** If you can cut it without losing meaning, cut it.
4. **One clear CTA.** Every email ends with exactly one thing the reader should do.
5. **No meta-commentary.** Never say "this email is to..." or "I am writing to inform you." Just say the thing.

## Humanizer Gate

After drafting, process through the `humanizer` skill in embedded mode. The humanizer handles all 33 AI-detection patterns. Email-specific checks on top of that:

- Zero em dashes (the #1 AI tell in emails)
- Zero banned openings or closings (see lists below)
- No corporate buzzwords: "synergy," "leverage," "circle back," "touch base," "loop in," "moving forward," "as per," "please be advised"
- No rule-of-three unless the content genuinely has three items
- Read the email aloud. If any line sounds like a template, rewrite it.

## Banned Openings

- "I hope this email finds you well"
- "I hope you are doing well"
- "I am writing to..." / "I wanted to reach out..."
- "I trust this message finds you in good health"
- "Per our conversation..." / "As per my last email..."
- "Hope you had a great weekend" / "Happy [weekday]"

## Banned Closings

- "Please do not hesitate to contact me"
- "I remain at your disposal"
- "Thanking you in anticipation"
- "Looking forward to your earliest convenience"
- "Please revert back"

## Output Format

Deliver exactly:

```
Subject: [subject line]

[email body]
```

No commentary before or after. No "Here is your email." Just the subject and the body. If the user asks for alternatives, provide a maximum of 2 variants with a one-line note on what differs.

## Example: Cold Email (Before/After)

**Before (AI-generated, every mistake at once):**

> Subject: Exploring Synergies in Cybersecurity Solutions
>
> Dear Mr. Johnson,
>
> I hope this email finds you well. I am writing to introduce myself and explore potential synergies between our organizations. Our company leverages cutting-edge penetration testing methodologies to enhance the security posture of enterprises across the landscape.
>
> We would love the opportunity to delve deeper into how we can add value to your security initiatives. Please do not hesitate to reach out at your earliest convenience.
>
> Warm regards,
> Muslum

**After (human, specific, concise):**

> Subject: Saw the exposed staging endpoint
>
> Hi James,
>
> I noticed your company's staging API is returning verbose error traces on the /v2/auth route. Not a crisis, but it leaks framework versions that make targeted attacks easier.
>
> I run security assessments for SaaS teams your size. Would it make sense to do a quick 20-minute walkthrough of what I found?
>
> Muslum
>
> P.S. Here's a redacted sample report from a similar engagement: [link]

**Why the second version works:** specific observation (not generic pitch), one clear ask (20-minute call), P.S. with proof, zero fluff.

## Red Flags: Stop and Rewrite

- More than 3 paragraphs in a cold email
- Opening with a pleasantry that adds zero information
- Subject line longer than 10 words
- No clear CTA at the end
- Multiple asks competing for attention
- "Just checking in" as the entire follow-up strategy

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Sounds robotic | Read it aloud. Rewrite anything that sounds scripted. |
| Too long | Cut the middle. Keep the hook and the ask. |
| No clear ask | End with one action the reader should take. |
| Wrong tone | Re-check the power dynamic from the grill. |
| Generic cold email | Add one specific, researched detail about the recipient. |
| Over-apologizing | One apology. Then the fix. Then move on. |
| Subject line is an afterthought | Write it last using the methodology above. |
