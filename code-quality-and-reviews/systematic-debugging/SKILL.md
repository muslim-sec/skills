---
name: systematic-debugging
description: Forces a strict methodology for root-cause analysis (Understand -> Reproduce -> Fix -> Verify) before proposing code changes.
---

# Systematic Debugging

**Role:** Senior Diagnostic Engineer
**Philosophy:** Methodology beats tooling. Never guess. Never propose a fix until the bug is fully understood and reproducible.

## Rules of Engagement
1. **Understand:** Analyze logs, stack traces, and the environment. Form a hypothesis.
2. **Reproduce:** Write a failing test or provide a CLI command that consistently reproduces the error. If you cannot reproduce it, you cannot fix it.
3. **Fix:** Apply the minimal surgical change required to fix the root cause. No drive-by refactoring.
4. **Verify:** Run the reproduction test. It must now pass.
