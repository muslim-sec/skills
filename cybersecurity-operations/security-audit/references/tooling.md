# Tooling: install, run, parse

Save raw output to `security-reports/raw/`. Prefer JSON/SARIF output so results can be merged. If a tool is unavailable and can't be installed, record "not run — <reason>" in the report.

## Contents
1. Secrets — Gitleaks, TruffleHog
2. SCA — npm/pnpm/yarn audit, OSV-Scanner, Trivy, OWASP Dependency-Check
3. SAST — Semgrep (SonarQube optional)
4. Headers & config — check_headers.py
5. Passive DAST — OWASP ZAP baseline
6. Container & IaC — Trivy config, Hadolint, Checkov
7. SBOM — Syft / CycloneDX, Dependency-Track
8. IAST, fuzzing, penetration testing — when and how to recommend

---

## 1. Secrets
**Gitleaks** (scans working tree + full git history)
```bash
# install: brew install gitleaks | or download release binary | or docker
docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest detect --source /repo --report-format json --report-path /repo/security-reports/raw/gitleaks.json --redact
# no-git (e.g. zip upload): add --no-git
```
**TruffleHog** (verifies whether keys are live — useful to prioritize)
```bash
docker run --rm -v "$PWD:/repo" trufflesecurity/trufflehog:latest git file:///repo --json --only-verified > security-reports/raw/trufflehog.json
```
Also check manually: `.env*` committed, `NEXT_PUBLIC_*` vars holding server secrets, keys in `next.config.js`, CI files, Dockerfiles, and the built client bundle (`grep -rE "sk_live|AKIA|-----BEGIN" .next/static` after a build).

Always report with `--redact` / masked values.

## 2. SCA (dependencies)
```bash
npm audit --json > security-reports/raw/npm-audit.json        # or: pnpm audit --json / yarn npm audit --json
npx --yes osv-scanner@latest --format json -r . > security-reports/raw/osv.json   # or the Go binary
docker run --rm -v "$PWD:/src" aquasec/trivy:latest fs --scanners vuln,license --format json /src > security-reports/raw/trivy-fs.json
```
OWASP Dependency-Check (Java/multi-ecosystem, slower, needs NVD API key for speed):
```bash
docker run --rm -v "$PWD:/src" owasp/dependency-check --scan /src --format JSON --out /src/security-reports/raw
```
Fixing: `npm audit fix` (non-breaking only). Never run `npm audit fix --force` without approval — it can apply major upgrades. For transitive issues use `overrides` (npm) / `pnpm.overrides` / `resolutions` (yarn). Also check framework advisories (e.g. Next.js security releases) and upgrade to the latest patch of the current major.

## 3. SAST
**Semgrep** (free, OSS rules)
```bash
pip install semgrep   # or: brew install semgrep | docker semgrep/semgrep
semgrep scan --config p/default --config p/owasp-top-ten --config p/secrets \
  --config p/nextjs --config p/react --config p/typescript \
  --json -o security-reports/raw/semgrep.json
```
Choose packs by stack: `p/django`, `p/flask`, `p/express`, `p/nodejsscan`, `p/php`, `p/golang`, `p/java`. Some registry packs may not exist for every framework — if a pack errors, drop it and continue.
SonarQube/SonarCloud: optional if the user already has it; read its results rather than setting it up from scratch.

Review every High/Error result in code context before calling it confirmed — SAST has a meaningful false-positive rate.

## 4. Headers & config
```bash
python3 scripts/check_headers.py https://example.com --json security-reports/raw/headers.json
```
Checks CSP (and unsafe-inline/unsafe-eval), frame-ancestors / X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, COOP, HSTS, cookie flags, server/x-powered-by disclosure, HTTP→HTTPS redirect, and presence of security.txt, robots.txt, site.webmanifest, humans.txt. Outputs a grade comparable to external scanners. Cross-check with securityheaders.com or Mozilla Observatory if the user wants a third-party confirmation.

## 5. Passive DAST — OWASP ZAP baseline
The baseline scan spiders the site and reports passively observed issues; it does not send attack traffic, so it is appropriate even for production with the owner's permission. Prefer staging anyway.
```bash
docker run --rm -v "$PWD/security-reports/raw:/zap/wrk:rw" -t ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t https://staging.example.com -J zap-baseline.json -r zap-baseline.html -m 3
```
For APIs with an OpenAPI spec: `zap-api-scan.py -t <openapi-url> -f openapi` — **staging only**, since it sends active test requests. Active/full scans (`zap-full-scan.py`) only on staging, with explicit user consent, and never against third-party hosts.

## 6. Container & IaC
```bash
docker run --rm -v "$PWD:/src" aquasec/trivy:latest config --format json /src > security-reports/raw/trivy-config.json   # Dockerfile, k8s, Terraform, Helm
docker run --rm -i hadolint/hadolint < Dockerfile
pip install checkov && checkov -d . -o json > security-reports/raw/checkov.json
docker run --rm aquasec/trivy:latest image <image:tag>   # if an image is built
```
Also review `vercel.json` / `netlify.toml` / CDN rules for header conflicts, open redirects in rewrite rules, and exposed preview deployments.

## 7. SBOM
```bash
npx --yes @cyclonedx/cyclonedx-npm --output-file security-reports/sbom.cdx.json
# or: syft dir:. -o cyclonedx-json > security-reports/sbom.cdx.json
```
Upload to Dependency-Track (self-hosted via Docker) for continuous CVE alerting.

## 8. IAST, fuzzing, penetration testing

These are usually recommended in the report rather than performed by the agent:

- **IAST/RASP** (e.g. Contrast Security): requires an agent installed in the runtime and an account. Recommend for Strict apps with complex server logic.
- **Fuzzing / API security testing** (e.g. StackHawk, Schemathesis for OpenAPI, language fuzzers like Jazzer.js or AFL++ for parsers): worthwhile when the app parses complex input (files, custom formats) or exposes a documented API. If the user wants it, run schema-based API testing against **staging** with their consent, and treat crashes/500s as findings.
- **Penetration testing**: the agent's part is preparation and self-review — threat model, authorization matrix (who can do what), the manual code-review checklist, and TestSprite access-control tests using the user's own test accounts. Confirming exploitability and chaining issues is work for an authorized human tester or an agentic pentest platform (e.g. XBOW, Escape) engaged by the owner under a written scope. Recommend this for Strict apps annually and before major launches; list the findings marked "Needs confirmation" as the starting scope.
