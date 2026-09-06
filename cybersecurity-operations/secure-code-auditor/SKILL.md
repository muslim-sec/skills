---
name: Secure Code Auditor
description: Performs static code analysis to detect OWASP Top 10 vulnerabilities and suggests secure coding fixes.
---

# Secure Code Auditor

Use this skill when the user provides source code and asks for a security review or vulnerability check.

## Capabilities
- **OWASP Top 10 Focus**: Scan code for Injection (SQLi, NoSQLi, XSS), Broken Authentication, Sensitive Data Exposure, IDOR, and Misconfigurations.
- **Secret Detection**: Identify hardcoded API keys, passwords, and tokens.
- **Dependency Review**: Check for outdated or vulnerable libraries.

## Guidelines
1. Never execute the code. Analyze it statically.
2. When a vulnerability is found, explain *why* it is dangerous, and provide the exact *secure code snippet* to fix it.
3. Suggest the use of parameterized queries, proper input validation, and output encoding.
