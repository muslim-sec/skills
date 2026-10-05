# Manual code review checklist

Focus on the threat model's assets and entry points. For each item, note file:line evidence. Use this to find weaknesses to fix — not to build attacks.

## Authentication & sessions
- Session/auth cookies: `HttpOnly`, `Secure`, `SameSite=Lax|Strict`, reasonable expiry, rotated on login.
- Password reset / magic-link tokens: single-use, expiring, not logged.
- Rate limiting / lockout on login, signup, reset, OTP endpoints.
- Auth library configured per docs (NextAuth/Auth.js `secret` set, `trustHost` understood; Supabase/Firebase rules not left open).

## Authorization (the #1 source of serious bugs)
- Every API route, server action, and route handler checks the session **and** ownership/role on the server — not only in UI.
- Object lookups filter by the current user/tenant (`where: { id, userId: session.user.id }`), not by ID alone.
- Admin paths protected server-side; middleware matchers actually cover them.
- Supabase: RLS enabled on every table with policies; service-role key never in client code. Firebase: security rules not `allow read, write: if true`.

## Input handling & output encoding
- No raw SQL string concatenation; ORM/parameterized queries only.
- `dangerouslySetInnerHTML`, `innerHTML`, `eval`, `new Function` — sanitized (DOMPurify) or removed.
- Server-side fetches of user-supplied URLs (SSRF): allowlist hosts, block internal IP ranges.
- Redirects to user-supplied URLs: allowlist.
- File uploads: type/size validation, stored outside web root or in object storage, no user-controlled paths.
- Schema validation (zod/yup) on every API input.

## Secrets & config
- Only public values in `NEXT_PUBLIC_*`. Server secrets only in server code.
- `.env*` in `.gitignore`; `.env.example` has placeholders only.
- Error pages don't leak stack traces in production; `x-powered-by` disabled (`poweredByHeader: false`).
- CORS not `*` with credentials.

## Webhooks & third parties
- Webhook signatures verified (Stripe, Paddle, etc.) using the raw body.
- Third-party scripts minimized; loaded with SRI where possible; listed in CSP.

## AI features (if present)
- User input to LLMs can't trigger privileged tools without server-side authz.
- LLM output rendered as text, not HTML; API keys server-side only; per-user usage limits.

## Data protection
- PII minimized in logs and analytics.
- Backups and storage buckets private.
