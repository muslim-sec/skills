---
name: security-audit
description: "Defensive application-security audit and hardening for apps the user owns — runs SAST, SCA/dependency, secret detection, container/IaC, security-header/cookie checks, passive DAST, and TestSprite functional/access-control tests, then fixes issues and writes an AI-executable fix plan plus a plain-language brief. Use this skill whenever the user asks to security-check, harden, audit, or \"make secure\" a website, web app, API, or repo; pastes findings from Rafter, securityheaders.com, Mozilla Observatory, Snyk, Dependabot, ZAP, Lighthouse or similar; mentions CSP, security headers, clickjacking, cookie flags, security.txt, leaked secrets, vulnerable packages, OWASP, or pre-launch security review; or asks to set up recurring security scans. Also trigger on Arabic requests like: فحص أمني، أمان الموقع، ثغرات، تأمين التطبيق. Built by Hossamudin Hassan — Mahara AI (maharaai.com)."
---

# Security Audit & Hardening

A structured, defensive security workflow for software the user owns or is authorized to test. It runs what can be run locally through the coding agent, uses TestSprite (via MCP) for live functional and access-control testing when available, fixes what it safely can, and ends with two deliverables: an **AI Fix Plan** precise enough for another agent to execute step by step, and a **Human Brief** the owner can read in two minutes.

The goal is not to produce a scary list of findings. It is to leave the app measurably safer, with evidence, and with a plan for keeping it that way.

## Ground rules (read first)

- **Authorization and scope come first.** Only scan code, domains, and environments the user owns or has written permission to test. Confirm this in Phase 1. If the target belongs to someone else and permission is unclear, stop and say so — scanning third-party sites can be illegal and can take production systems down.
- **Defensive only.** This skill finds and fixes weaknesses using established scanners and code review. It does not write exploit code, attack payloads, or instructions for abusing a flaw. Where a finding would need exploitation to confirm, record it as "needs confirmation" and recommend an authorized professional or platform pentest (see `references/tooling.md` → Penetration testing).
- **Prefer staging over production** for any active/dynamic scanning. Passive checks (headers, cookies, well-known files) are fine against production.
- **Never print secrets.** When a secret is found, show file, line, and type with the value masked (first 4 chars + `…`). Treat it as compromised: rotation comes before deletion from code.
- **Don't break the app.** Roll out CSP in `Report-Only` first when unsure, run the build and tests after each fix batch, and keep changes small and reviewable.

## Workflow

### Phase 1 — Intake & scoping

Gather this before running anything. Use the AskUserQuestion tool when available (one round, up to 4 questions); infer what you can from the repo first so you only ask what's unknown.

1. **Target**: repo path and/or live URL(s); staging URL if one exists.
2. **Authorization**: "I own this / I'm authorized to test it" — required.
3. **Assurance profile** (sets which phases run; details in `references/profiles.md`):
   - **Essentials** — landing pages, marketing sites, blogs: headers, cookies, secrets, dependencies.
   - **Standard** (default) — apps with login, forms, payments via third party: Essentials + SAST + passive DAST + TestSprite functional/authz.
   - **Strict** — handles money, health, PII at scale, multi-tenant SaaS: Standard + IaC/container, SBOM, deeper authz matrix, recommend external pentest.
4. **Skips & constraints**: checks to skip, no-touch files, deadlines, whether auto-fixing is allowed or report-only.

If the user pasted an external audit (e.g. Rafter), parse every item into the findings list now — each becomes a finding with its original ID/status preserved, so the report can show "external finding → fixed/verified".

### Phase 2 — Recon & tool detection

Run `bash scripts/detect_env.sh <repo-path>` to detect stack (Next.js, Express, Django, etc.), package managers, hosting config (`vercel.json`, `netlify.toml`, Dockerfile, Terraform, k8s), CI, and which scanners are installed. Install missing free tools only with the user's OK (commands in `references/tooling.md`). If a tool can't be installed, note it as "not run" in the report — never silently skip.

Check for the TestSprite MCP (tools named like `testsprite_bootstrap`). If absent and the profile is Standard/Strict, offer setup per `references/testsprite.md` — the user needs a TestSprite account and API key. Continue with other phases while they decide.

Write a short threat model (5–10 lines): what the app does, its assets (accounts, payments, PII, admin), entry points (forms, APIs, uploads, webhooks), trust boundaries. This focuses the review on what actually matters for this app.

### Phase 3 — Scans

Run the phases the profile selects. Commands, flags, and output parsing are in `references/tooling.md`. Save raw outputs to `security-reports/raw/` (add that folder to `.gitignore` — raw output can contain secret locations).

| Phase | What | Default tools | Profile |
|---|---|---|---|
| 3a Config & headers | Security headers, cookie flags, HTTPS/HSTS, well-known files | `scripts/check_headers.py` | All |
| 3b Secrets | Code + full git history | Gitleaks (TruffleHog as second opinion) | All |
| 3c SCA | Vulnerable/outdated deps, licenses | `npm audit` / `pnpm audit`, OSV-Scanner, Trivy fs | All |
| 3d SAST | Code-level flaws | Semgrep (`p/default`, `p/owasp-top-ten`, framework packs) | Standard+ |
| 3e Manual code review | Authz, input handling, SSRF, file upload, secrets in client bundle, server actions | Agent review guided by `references/code-review-checklist.md` | Standard+ |
| 3f Passive DAST | Runtime issues seen by a crawler, no attack traffic | OWASP ZAP baseline scan (Docker) on staging | Standard+ |
| 3g Functional & authz | Login, roles, cross-user access, session handling as real users | TestSprite MCP | Standard+ |
| 3h Container & IaC | Dockerfile, k8s, Terraform, CI config | Trivy config, Checkov/Hadolint | Strict (or if files exist) |
| 3i SBOM | Inventory for ongoing monitoring | Syft or `cyclonedx-npm` → Dependency-Track | Strict |

IAST, RASP, fuzzing, and agentic pentest platforms (XBOW, Escape, StackHawk, Contrast) usually need accounts, agents, or paid plans; describe them as recommendations in the report with when they'd be worth it, rather than attempting them.

### Phase 4 — Triage

Merge every result into one findings list. For each finding:

- De-duplicate across tools (same root cause = one finding, multiple evidence lines).
- Assign severity: **Critical / High / Medium / Low / Info** using `references/severity.md` (exploitability × impact in *this* app's context, not the tool's default label).
- Mark confidence: **Confirmed** (evidence reproduces), **Likely**, **Needs confirmation**. Drop clear false positives but list them in an appendix with the reason — this saves the next audit from re-investigating.
- Give it a stable ID: `SEC-<CATEGORY>-<NNN>` (e.g. `SEC-HDR-001`, `SEC-SECRET-002`, `SEC-DEP-003`).

### Phase 5 — Fix (if allowed)

Fix in this order, committing (or at least grouping) per batch so each is easy to review and revert:

1. **Leaked secrets** — tell the user to rotate/revoke first (you can't do it for them), then remove from code, move to env vars, and consider history rewrite only after rotation.
2. **Critical/High code and dependency issues** — patch-level upgrades first; flag major-version upgrades for user approval.
3. **Headers, cookies, well-known files** — see `references/nextjs-hardening.md` for exact Next.js / Vercel implementations (CSP with nonces, `frame-ancestors`, cookie flags, `security.txt`, `site.webmanifest`, `humans.txt`).
4. **Medium/Low** as time allows.

After each batch: run the build, lint, and existing tests. If something breaks, revert that change and record it as "fix blocked" with the reason. For anything you did not fix, the AI Fix Plan must contain the exact steps.

### Phase 6 — Verify

Re-run the specific check that found each fixed issue and record before/after evidence (e.g. header grade F → A, `gitleaks` 3 → 0, audit count). Verification against the live site only works after deploy — if not deployed, mark "fixed in code, pending deploy verification" and give the one-line command to confirm.

### Phase 7 — Report

Produce both documents using `references/report-template.md`:

- `security-reports/SECURITY_FIX_PLAN.md` — **for AI agents**. Always English (precision). Ordered, atomic tasks with exact file paths, code, commands, acceptance criteria, and verify commands, plus a machine-readable `findings.json`.
- `security-reports/SECURITY_BRIEF.md` (or the language of the user — Arabic users get Arabic) — **for humans**. Score, top risks in plain words, what was fixed, what they must do personally (e.g. rotate a key), and the next-steps schedule.

Deliver the files per the environment's normal file-delivery method and summarize in 3–5 sentences in chat.

### Phase 8 — Keep it secure (maintenance & scheduling)

Security decays as dependencies age and code changes. Recommend a cadence from `references/maintenance.md` based on the profile, and offer — don't impose — to set it up:

- **CI**: drop `assets/security-ci.yml` into `.github/workflows/` (Gitleaks + Semgrep + dependency audit on every PR, weekly full scan) and enable Dependabot via `assets/dependabot.yml`.
- **Scheduled agent runs**: if the environment offers scheduled tasks, offer to schedule a recurring re-run of this skill (e.g. weekly Essentials, monthly Standard) that compares against the last `findings.json` and reports only what changed.
- **Monitoring**: SBOM in Dependency-Track, uptime/header monitoring, and an annual or pre-major-launch external pentest for Strict apps.

Tell the user explicitly which checks should be re-run after deploy, which should run on every PR, and which only periodically.

## Handling pasted audit findings (e.g. Rafter)

Many users arrive with a report from an external scanner. Map each item to a category, then treat it like any other finding:

- Missing headers (CSP, X-Frame-Options/frame-ancestors, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, COOP) → one grouped finding `SEC-HDR-*`, fixed in one place (`next.config.js` `headers()` or `middleware.ts` for nonce CSP). Avoid setting the same header in both the app and `vercel.json`/CDN.
- Cookie flags (e.g. `NEXT_LOCALE` missing Secure/HttpOnly) → judge by purpose: a locale cookie holds no secret and next-intl may read it client-side, so `Secure` + `SameSite=Lax` is required while `HttpOnly` is optional; session/auth cookies need all three. Explain this nuance rather than blindly applying every flag.
- `security.txt` missing → add `public/.well-known/security.txt` (RFC 9116, with `Expires`).
- `site.webmanifest`, `humans.txt`, canonical tag → Info/SEO items; implement quickly, mark as non-security in the brief.
- Aggregate grade (e.g. "F 14/100") → not a separate fix; it's the outcome metric. Report before/after.

## Reference files

- `references/profiles.md` — what each assurance profile includes and intake question wording.
- `references/tooling.md` — install and run commands per scanner, output parsing, penetration-testing guidance.
- `references/nextjs-hardening.md` — Next.js/Vercel headers, CSP (nonce + report-only rollout), cookies, well-known files.
- `references/code-review-checklist.md` — what to look for in manual review, by area.
- `references/testsprite.md` — MCP setup, verification, workflow, and using it for authz testing.
- `references/severity.md` — severity rubric and confidence levels.
- `references/report-template.md` — exact structure of the AI Fix Plan, findings.json, and Human Brief.
- `references/maintenance.md` — recurring cadence, CI, scheduling, monitoring.
- `scripts/detect_env.sh` — stack and tool detection.
- `scripts/check_headers.py` — header/cookie/well-known-file grader with JSON output.
- `assets/security-ci.yml`, `assets/dependabot.yml`, `assets/security.txt` — templates.
