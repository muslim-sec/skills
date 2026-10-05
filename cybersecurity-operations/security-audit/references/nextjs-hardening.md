# Next.js / Vercel hardening

Set each header in **one** layer only. If `vercel.json`, a CDN (Cloudflare), and `next.config.js` all set headers, pick one and remove the others — duplicate CSP headers are combined by browsers as an intersection and break things unpredictably.

## 1. Static security headers (`next.config.js` / `next.config.mjs` / `next.config.ts`)

```js
const securityHeaders = [
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'X-Frame-Options', value: 'DENY' },                       // or SAMEORIGIN if the site embeds itself
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()' },
  { key: 'Cross-Origin-Opener-Policy', value: 'same-origin' },      // use 'same-origin-allow-popups' if OAuth/payment popups break
  { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' }, // Vercel sets HSTS on its domains; keep one source
];

const nextConfig = {
  poweredByHeader: false,
  async headers() {
    return [{ source: '/:path*', headers: securityHeaders }];
  },
};
module.exports = nextConfig; // or export default
```
Merge into the existing config — don't overwrite other keys (i18n, images, redirects). If the project uses `next-intl`/`next-pwa`/other wrappers, keep the wrapper: `module.exports = withNextIntl(nextConfig)`.

Permissions-Policy: only deny features the app doesn't use. Check for `getUserMedia`, `geolocation`, Payment Request, and embedded widgets (YouTube, Calendly, Stripe) before denying.

## 2. Content-Security-Policy

### Option A — Nonce-based CSP via middleware (recommended for App Router, strongest)
Requires dynamic rendering for pages (nonces can't be baked into static HTML).
```ts
// middleware.ts
import { NextResponse, type NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64');
  const isDev = process.env.NODE_ENV !== 'production';
  const csp = [
    `default-src 'self'`,
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${isDev ? " 'unsafe-eval'" : ''}`,
    `style-src 'self' 'nonce-${nonce}'`,
    `img-src 'self' blob: data: https:`,
    `font-src 'self' data:`,
    `connect-src 'self'`,              // add API/analytics origins
    `frame-src 'self'`,                // add embeds (youtube-nocookie, stripe, calendly)
    `object-src 'none'`,
    `base-uri 'self'`,
    `form-action 'self'`,
    `frame-ancestors 'none'`,
    `upgrade-insecure-requests`,
  ].join('; ');

  const requestHeaders = new Headers(request.headers);
  requestHeaders.set('x-nonce', nonce);
  requestHeaders.set('Content-Security-Policy', csp);

  const response = NextResponse.next({ request: { headers: requestHeaders } });
  response.headers.set('Content-Security-Policy', csp); // use 'Content-Security-Policy-Report-Only' during rollout
  return response;
}

export const config = {
  matcher: [{ source: '/((?!api|_next/static|_next/image|favicon.ico).*)',
              missing: [{ type: 'header', key: 'next-router-prefetch' }, { type: 'header', key: 'purpose', value: 'prefetch' }] }],
};
```
Read the nonce in server components where you render `<Script>`: `const nonce = (await headers()).get('x-nonce')` and pass `nonce={nonce}`. Next.js applies the nonce to its own scripts automatically when the CSP request header is present.

**If a middleware already exists** (next-intl, auth), compose: run the existing middleware to get its response, then set the CSP headers on that response. Don't create a second `middleware.ts`.

Tailwind/CSS-in-JS: if inline styles break, `style-src 'self' 'unsafe-inline'` is an accepted, lower-risk compromise (style injection is far less dangerous than script injection) — document it.

### Option B — Static CSP in `headers()` (simpler, for mostly static sites)
Next.js injects inline scripts for hydration, so a static CSP without nonces typically needs `'unsafe-inline'` in `script-src`. That still gives `frame-ancestors`, `object-src`, `base-uri`, `form-action`, and source allowlisting, but won't satisfy "no unsafe-inline" checks. Say this explicitly and prefer Option A when the scanner requirement matters.

### Rollout
1. Ship as `Content-Security-Policy-Report-Only` with `report-to`/`report-uri` (or just watch the browser console) for a few days.
2. Browse every key page: home, auth, checkout, dashboards, embeds, analytics. Add needed origins.
3. Switch to enforcing `Content-Security-Policy`.
Common origins to add: Google Analytics/GTM (`https://www.googletagmanager.com`, `https://www.google-analytics.com`), Vercel Analytics (`https://va.vercel-scripts.com`), Supabase (`https://<ref>.supabase.co`, `wss://<ref>.supabase.co`), Stripe (`https://js.stripe.com`, frame `https://*.stripe.com`).

## 3. Clickjacking
`frame-ancestors 'none'` (CSP) + `X-Frame-Options: DENY` (legacy browsers). If the site must be embeddable by a partner: `frame-ancestors 'self' https://partner.com` and drop XFO (it can't express allowlists).

## 4. Cookies
- **Auth/session cookies**: `HttpOnly; Secure; SameSite=Lax` (Strict if no cross-site entry needed). Configure in the auth library, not by hand.
- **`NEXT_LOCALE`** (next-intl/Next i18n): holds only a locale code — no secret. Add `Secure` and `SameSite=Lax`. `HttpOnly` is safe only if no client code reads the cookie; next-intl reads it in middleware (server), so it's usually fine, but check for `document.cookie` usage first.
  ```ts
  // next-intl v3.x+/v4: in routing config
  export const routing = defineRouting({
    locales: ['ar', 'en'], defaultLocale: 'ar',
    localeCookie: { name: 'NEXT_LOCALE', sameSite: 'lax', secure: true, maxAge: 60 * 60 * 24 * 365 }
  });
  ```
  If the cookie is set manually: `response.cookies.set('NEXT_LOCALE', locale, { secure: true, httpOnly: true, sameSite: 'lax', path: '/', maxAge: 31536000 })`. Check the installed next-intl version's docs for exact option names.

## 5. Well-known & meta files (put in `public/`)
- `public/.well-known/security.txt` — see `assets/security.txt`. `Contact` and `Expires` are required (RFC 9116); renew `Expires` within a year (add to maintenance).
- `site.webmanifest` — App Router: `app/manifest.ts` returning `MetadataRoute.Manifest` (served at `/manifest.webmanifest`); some scanners look for `/site.webmanifest` specifically, so a `public/site.webmanifest` plus `<link rel="manifest">` satisfies both.
  ```ts
  import type { MetadataRoute } from 'next';
  export default function manifest(): MetadataRoute.Manifest {
    return { name: 'Site Name', short_name: 'Site', start_url: '/', display: 'standalone',
      background_color: '#ffffff', theme_color: '#0f172a', lang: 'ar', dir: 'rtl',
      icons: [{ src: '/icon-192.png', sizes: '192x192', type: 'image/png' }, { src: '/icon-512.png', sizes: '512x512', type: 'image/png' }] };
  }
  ```
- `public/humans.txt` — optional credits, no personal emails.
- Canonical: App Router `export const metadata = { metadataBase: new URL('https://www.example.com'), alternates: { canonical: '/' } }` — ensure per-locale pages have correct canonicals + `hreflang` alternates.

## 6. Vercel-only (no Next config access)
```json
{ "headers": [{ "source": "/(.*)", "headers": [
  { "key": "X-Content-Type-Options", "value": "nosniff" },
  { "key": "X-Frame-Options", "value": "DENY" },
  { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
  { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
  { "key": "Cross-Origin-Opener-Policy", "value": "same-origin" }
]}]}
```

## 7. Verify
```bash
curl -sI https://www.example.com | grep -iE 'content-security|x-frame|x-content-type|referrer|permissions|cross-origin-opener|strict-transport|set-cookie'
curl -s https://www.example.com/.well-known/security.txt
python3 scripts/check_headers.py https://www.example.com
```
Then browse the site with DevTools console open and confirm no CSP violations.
