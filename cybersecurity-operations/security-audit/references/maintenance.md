# Keeping it secure

## What to re-run, and when

| Check | Trigger | Why |
|---|---|---|
| Secrets (Gitleaks) | Every commit/PR (pre-commit + CI) | Leaks happen at commit time; catching them before push avoids rotation |
| SAST (Semgrep) | Every PR | New code = new flaws |
| SCA (audit / OSV / Dependabot) | Every PR + weekly | New CVEs are published daily against unchanged code |
| Headers/cookies (`check_headers.py`) | After every deploy + weekly | CDN/config changes silently drop headers |
| ZAP baseline | Weekly on staging, after major releases | Runtime regressions |
| TestSprite suite | Before releases touching auth/roles/payments | Access-control regressions are the costliest bugs |
| IaC/container (Trivy) | When infra files change + monthly | Base images accumulate CVEs |
| SBOM → Dependency-Track | Every release | Continuous alerting on newly disclosed CVEs |
| Full audit (this skill) | Monthly (Standard) / quarterly deep review (Strict) | Catch drift, review threat model |
| External pentest | Annually and before major launches (Strict) | Humans find chained logic flaws tools miss |

## Setting it up
1. **CI**: copy `assets/security-ci.yml` → `.github/workflows/security.yml`. Copy `assets/dependabot.yml` → `.github/dependabot.yml`. Enable GitHub secret scanning + push protection in repo settings (free for public repos; GitHub Advanced Security for private).
2. **Pre-commit**: `gitleaks protect --staged` via a pre-commit hook (husky or `.git/hooks/pre-commit`).
3. **Scheduled agent re-runs**: if the host offers scheduled tasks, offer to create one. The scheduled prompt must be standalone, e.g.:
   > "Run the security-audit skill on <repo/URL> with the <profile> profile, compare against security-reports/findings.json from the previous run, fix new Low/Medium items automatically if allowed, and send me a brief listing only new, fixed, and still-open findings."
   Ask for cadence (weekly/monthly) and confirm before creating.
4. **Monitoring**: Dependency-Track (self-hosted, free) ingests the CycloneDX SBOM and alerts on new CVEs. For runtime protection consider a WAF (Vercel Firewall, Cloudflare) and, for Strict apps, RASP/IAST vendors (Contrast, etc.).
5. **Patch policy**: patch/minor updates weekly via Dependabot; majors reviewed monthly; Critical CVEs within 24–48h.
