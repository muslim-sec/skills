---
name: GitHub Security Guard
description: Scans code for hardcoded secrets, API keys, and vulnerabilities before committing to GitHub.
---

# GitHub Security Guard

This skill acts as a strict firewall between your local code and public GitHub repositories.

## Pre-Commit Audit Steps
1. **Secret Scanning**: Scan all modified files for strings resembling API keys, JWT tokens, AWS keys, or database passwords (e.g., Supabase URIs).
2. **Environment Variables**: Ensure all secrets are safely stored in `.env` files and that `.env` is listed in `.gitignore`.
3. **Sanitization**: If a secret is found, immediately halt the commit process and alert the user to remove it.

## Best Practices
- Recommend the user to install tools like `gitleaks` or `git-secrets` as local pre-commit hooks.
- Treat all string literals containing "key", "secret", "token", "password" as highly suspicious.
