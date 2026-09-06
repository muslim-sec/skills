---
name: bash-expert
description: >-
  Strict architectural standards for writing enterprise-grade, safe, and maintainable Bash scripts.
---

# Enterprise Bash Architecture

When writing or modifying Bash scripts, you MUST adhere to the following strict standards:

## 1. The Safe Bash Header
Every Bash script must start with the strict mode header to prevent hidden failures:
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
```
- `set -e`: Exit immediately if a command fails.
- `set -u`: Treat unset variables as an error.
- `set -o pipefail`: Return the exit status of the last command in the pipe that failed.

## 2. Architecture & Modularity
- Do not write monolithic scripts. Break logic into functions.
- Every function must declare local variables: `local var_name="value"`
- Use a `main` function and call it at the end of the script:
  ```bash
  main() {
      setup
      process_data
  }
  main "$@"
  ```

## 3. Variable Expansion and Safety
- ALWAYS quote variables to prevent word splitting and globbing: `"$VAR"`, never `$VAR`.
- Use `${VAR:-default}` for fallback values.

## 4. Logging & Colored Output
- Do not use raw `echo` for logs. Create logging functions that write to stderr:
  ```bash
  log_info() { echo -e "\033[1;34m[INFO]\033[0m $*" >&2; }
  log_err()  { echo -e "\033[1;31m[ERROR]\033[0m $*" >&2; }
  ```
- Send all logging to `>&2` (stderr) so `stdout` remains clean.

## 5. Code Quality
- All scripts must pass `shellcheck` without warnings.
- Avoid using `eval`.
