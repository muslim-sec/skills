# Assurance profiles

Not every app needs the same depth. Pick the lightest profile that matches the real risk, and let the user override.

| | Essentials | Standard (default) | Strict |
|---|---|---|---|
| Typical app | Marketing site, blog, docs, portfolio | SaaS/app with login, forms, dashboards, third-party payments | Handles money directly, health/financial data, PII at scale, multi-tenant, regulated |
| Headers/cookies/well-known | ✅ | ✅ | ✅ |
| Secrets (code + history) | ✅ | ✅ | ✅ |
| SCA (deps) | ✅ | ✅ | ✅ + license review |
| SAST (Semgrep) | optional | ✅ | ✅ + custom rules |
| Manual code review | light | ✅ focused on threat model | ✅ full checklist |
| Passive DAST (ZAP baseline) | optional | ✅ (staging) | ✅ (staging) |
| TestSprite functional + authz | – | ✅ | ✅ with full role matrix |
| Container / IaC | if files exist | if files exist | ✅ |
| SBOM + Dependency-Track | – | optional | ✅ |
| External pentest | – | before big launch | ✅ annually + major releases |
| Re-run cadence | monthly | weekly CI + monthly full | per-PR CI + weekly full + quarterly review |

## Intake questions (suggested wording)

1. "What should I test?" — repo path / live URL / staging URL.
2. "Do you own this app or have permission to test it?" — Yes (owner) / Yes (authorized in writing) / Not sure → stop if not sure.
3. "What level of checking fits this app?" — Essentials / Standard (Recommended) / Strict, each with the one-line description above.
4. "Anything to skip or protect?" — multiSelect: Skip DAST / Skip TestSprite / Report only, don't change code / Don't upgrade major versions.

Infer answers from context where obvious (e.g. a pasted Rafter report already names the domain and stack).
