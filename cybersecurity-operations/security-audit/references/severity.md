# Severity & confidence rubric

Score each finding in the context of *this* app. A tool's default label is an input, not the answer.

| Severity | Meaning | Examples | Fix target |
|---|---|---|---|
| Critical | Direct compromise of data, accounts, or infrastructure with little effort | Live cloud/DB/payment key in repo or client bundle; auth bypass; one user can read another user's data; known-exploited RCE in a reachable dependency | Now (same day) |
| High | Serious impact, needs some conditions | Stored XSS vector; missing authz on an admin API; SQL built from user input; vulnerable dep with public exploit and reachable code path; session cookie without HttpOnly | This week |
| Medium | Real weakness, limited impact or hard to reach | Missing CSP; no clickjacking protection on pages with actions; verbose errors leaking stack traces; missing rate limiting on login | This sprint |
| Low | Hardening / defense in depth | Missing Referrer-Policy, Permissions-Policy, COOP; non-sensitive cookie missing Secure; outdated but not vulnerable deps | Backlog |
| Info | Best practice / non-security | security.txt, humans.txt, site.webmanifest, canonical tag | When convenient |

Raise one level when: the app handles payments/health/PII, the issue is on an unauthenticated path, or it chains with another finding. Lower one level when: the affected code is unreachable, behind strong auth for trusted admins only, or already mitigated elsewhere (document where).

## Confidence
- **Confirmed** — reproduced with evidence (header output, test failure, secret match verified as real format).
- **Likely** — strong static evidence, not reproduced at runtime.
- **Needs confirmation** — plausible; requires runtime testing, owner knowledge, or an authorized pentest.

## Scoring (for the brief)
Start at 100. Subtract per open finding: Critical 25, High 10, Medium 4, Low 1, Info 0. Floor at 0. Grade: A ≥ 90, B ≥ 80, C ≥ 65, D ≥ 50, F < 50. Report before and after fixes.
