# Report templates

Produce three files in `security-reports/` (dated copies optional: `security-reports/2026-09-19/`):
1. `SECURITY_FIX_PLAN.md` — for AI agents (English).
2. `findings.json` — machine-readable, used by the next run for diffing.
3. `SECURITY_BRIEF.md` — for humans, in the user's language.

Accuracy rules for the fix plan — these are what make it executable "step by step" by another agent without guessing:
- Every path is exact and relative to repo root; every code block is complete (no "..." inside code the agent must write), or is a precise diff against quoted existing lines.
- Every task says what to do if the file/assumption differs ("If `middleware.ts` exists, compose instead of replacing").
- Every task has an acceptance criterion and a verify command with its expected output.
- Tasks are ordered by dependency, then severity. One task = one logical change.
- Anything requiring a human (rotating keys, DNS, dashboard settings, paid tools) is marked `OWNER ACTION` and never faked as done.
- State facts only from evidence gathered; label assumptions as assumptions.

---

## SECURITY_FIX_PLAN.md

```markdown
# Security Fix Plan — <app/domain>
Generated: <date> · Profile: <Essentials|Standard|Strict> · Stack: <e.g. Next.js 15 App Router, next-intl, Vercel>
Repo: <path/commit SHA> · Live: <URL> · Scanned by: security-audit skill (Mahara AI)

## Execution rules for the agent
- Execute tasks in order. After each task run its Verify step; do not continue past a failing verify — fix or stop and report.
- Run `<build command>` and `<test command>` after each batch marked [BATCH END].
- Do not modify files outside those listed in a task without noting it.
- Never print secret values.

## Status summary
| ID | Title | Severity | Confidence | Status |
|----|-------|----------|-----------|--------|
| SEC-SECRET-001 | Stripe live key in lib/pay.ts | Critical | Confirmed | Open — OWNER ACTION |
| SEC-HDR-001 | Missing security headers (CSP, XFO, …) | Medium | Confirmed | Fixed in code, pending deploy |
...

## Tasks

### TASK 1 — SEC-XXX-NNN: <imperative title>
- **Severity / confidence:** High / Confirmed
- **Source:** <tool(s) + rule ID, or external audit item e.g. "Rafter item 4">
- **Evidence:** `<file>:<line>` / command output excerpt (masked)
- **Why it matters:** one sentence.
- **Preconditions:** e.g. "Next.js ≥13.4; no existing middleware.ts" (and what to do if false)
- **Steps:**
  1. Open `<path>`.
  2. Replace:
     ```ts
     <exact existing code>
     ```
     with:
     ```ts
     <exact new code>
     ```
  3. …
- **Acceptance criteria:** bullet list of observable outcomes.
- **Verify:**
  ```bash
  <command>
  ```
  Expected: `<exact expected output or pattern>`
- **Rollback:** how to revert if it breaks something.
[BATCH END]

## OWNER ACTIONS (human required)
1. Rotate <key type> in <provider dashboard> — then update env var `<NAME>` in <hosting>. Deadline: <today>.

## Not run / limitations
- <tool> not run: <reason>. Recommended: <how to run it>.

## Appendix A — False positives dismissed (with reason)
## Appendix B — Non-security defects found
## Appendix C — Raw outputs index (`security-reports/raw/*`)
```

---

## findings.json

```json
{
  "schema": "mahara-security-audit/v1",
  "target": { "repo": "", "commit": "", "urls": [""], "stack": "" },
  "profile": "standard",
  "generated_at": "ISO-8601",
  "score": { "before": 14, "after": 88, "grade_before": "F", "grade_after": "B" },
  "tools": [{ "name": "gitleaks", "version": "", "ran": true, "note": "" }],
  "findings": [{
    "id": "SEC-HDR-001",
    "title": "",
    "category": "headers|secrets|dependency|sast|authz|auth|input|config|iac|container|info",
    "severity": "critical|high|medium|low|info",
    "confidence": "confirmed|likely|needs_confirmation",
    "status": "open|fixed|fixed_pending_deploy|fix_blocked|owner_action|accepted_risk|false_positive",
    "source": ["rafter:item-4", "check_headers"],
    "locations": [{ "file": "", "line": 0, "url": "" }],
    "evidence": "masked excerpt",
    "fix_task": "TASK 3",
    "verify": "command",
    "cwe": "CWE-1021",
    "owasp": "A05:2021"
  }]
}
```
On re-runs, compare IDs/fingerprints with the previous `findings.json` and classify each as new / still open / fixed / regressed.

---

## SECURITY_BRIEF.md (human)

Keep it to one screen. Plain words, no jargon without a 3-word explanation. Match the user's language (Arabic for Arabic speakers; RTL-friendly Markdown).

```markdown
# Security Brief — <app>  (<date>)

**Score:** F (14) → B (88) after fixes · **Profile:** Standard

## Bottom line
2–3 sentences: how safe is it now, what's the single most important thing left.

## You need to do (only you can)
- [ ] Rotate the Stripe key that was in the code — today. (Why: anyone with the code could charge cards.)
- [ ] Deploy the changes, then run: `<one verify command>`

## What we fixed
- Added browser security protections (headers) → stops clickjacking and limits script injection.
- …

## Still open (and when to handle it)
| Issue | Risk in plain words | When |
|---|---|---|

## Keeping it safe
- Every PR: automatic secret + code + dependency checks (CI file added).
- Weekly/monthly: <scheduled re-run if set up, or offer>.
- Yearly / before big launch: external penetration test (recommended for <reason>).

## What was checked
✅ Headers & cookies · ✅ Secrets · ✅ Dependencies · ✅ Code scan · ⏭️ TestSprite (not set up) · …

_Security audit by the Mahara AI security-audit skill — maharaai.com_
```
