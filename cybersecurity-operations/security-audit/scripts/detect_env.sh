#!/usr/bin/env bash
# Detect stack, hosting/infra files, CI, and installed security tools.
# Usage: bash detect_env.sh [repo-path]
ROOT="${1:-.}"; cd "$ROOT" || exit 1
echo "== Repo: $(pwd)"
[ -d .git ] && echo "git: yes ($(git rev-parse --short HEAD 2>/dev/null), $(git rev-list --count HEAD 2>/dev/null) commits)" || echo "git: no (history scan not possible)"

echo "== Stack"
if [ -f package.json ]; then
  node -e '
    const p=require("./package.json"); const d={...p.dependencies,...p.devDependencies};
    const pick=["next","react","express","fastify","@nestjs/core","next-intl","next-auth","@auth/core","@supabase/supabase-js","firebase","prisma","@prisma/client","drizzle-orm","stripe","vite","nuxt","svelte","astro"];
    for (const k of pick) if (d[k]) console.log("  "+k+"@"+d[k]);
    console.log("  scripts:", Object.keys(p.scripts||{}).join(", "));' 2>/dev/null || echo "  package.json present (node not available to parse)"
fi
for f in pnpm-lock.yaml yarn.lock package-lock.json bun.lockb requirements.txt pyproject.toml Pipfile.lock go.mod Gemfile.lock composer.lock pom.xml build.gradle Cargo.toml; do
  [ -f "$f" ] && echo "  manifest: $f"
done
ls next.config.* 2>/dev/null | sed 's/^/  next config: /'
ls middleware.* src/middleware.* 2>/dev/null | sed 's/^/  middleware: /'
[ -d app ] || [ -d src/app ] && echo "  Next.js App Router detected"
[ -d pages ] || [ -d src/pages ] && echo "  pages/ directory detected"

echo "== Hosting / infra"
for f in vercel.json netlify.toml Dockerfile docker-compose.yml docker-compose.yaml fly.toml render.yaml app.yaml firebase.json supabase/config.toml; do
  [ -f "$f" ] && echo "  $f"
done
find . -path ./node_modules -prune -o \( -name '*.tf' -o -name 'Chart.yaml' -o -name '*.k8s.yaml' \) -print 2>/dev/null | head -5 | sed 's/^/  /'
[ -d .github/workflows ] && echo "  CI: GitHub Actions ($(ls .github/workflows | tr '\n' ' '))"
[ -f .github/dependabot.yml ] && echo "  Dependabot: configured" || echo "  Dependabot: not configured"
[ -f .gitlab-ci.yml ] && echo "  CI: GitLab"

echo "== Sensitive files tracked in git"
if [ -d .git ]; then
  git ls-files | grep -E '(^|/)\.env($|\.)|\.pem$|\.key$|id_rsa|credentials\.json|serviceAccount' | grep -v -E '\.env\.(example|sample|template)$' | sed 's/^/  TRACKED: /' || true
fi
grep -qE '^\.env' .gitignore 2>/dev/null && echo "  .env ignored: yes" || echo "  .env ignored: NO / unknown"

echo "== Tools"
for t in node npm pnpm yarn python3 pip docker git gitleaks trufflehog semgrep trivy osv-scanner checkov hadolint syft; do
  if command -v "$t" >/dev/null 2>&1; then echo "  [x] $t"; else echo "  [ ] $t"; fi
done
command -v node >/dev/null && echo "  node version: $(node -v) (TestSprite MCP needs >= 22)"
