---
name: better-cli
description: >-
  Best practices for building robust, human-friendly, and automation-ready CLI tools.
  Focuses on TTY awareness, colored output, separating data from logs, and graceful exits.
---

# Better CLI Architecture

When building Command Line Interfaces (CLI), follow these architectural rules:

## 1. TTY Awareness (Colors and Interactivity)
- Always check if the environment is a real terminal (TTY) before outputting colors or interactive prompts.
- In Node.js: `process.stdout.isTTY`
- In Python: `sys.stdout.isatty()`
- In Bash: `[ -t 1 ]`
- If NOT a TTY, disable all colors, animations, spinners, and interactive prompts. Output raw plain text for pipelines.

## 2. Stdout vs. Stderr Separation
- **stdout (Standard Output):** ONLY use for the actual data/result of the command. If the user pipes your command `cli > output.json`, only the pure data should go into that file.
- **stderr (Standard Error):** Use for ALL logs, warnings, errors, progress bars, and "Starting..." messages. Do not pollute stdout with logs.

## 3. Exit Codes
- `0`: Success
- `1`: General Error
- `2`: Invalid arguments / Usage error
- Always exit gracefully. Do not dump raw stack traces to the user unless in debug mode.

## 4. Argument Parsing
- Use robust parsers (e.g., `argparse` in Python, `commander`/`yargs` in Node, `pflag` in Go).
- Always provide a `-h` / `--help` and `-v` / `--version` flag.

## 5. Visual Polish
- Use terminal coloring libraries (e.g., `chalk` for Node, `rich` for Python, `fatih/color` for Go) when running in a TTY.
- Use ASCII/Unicode spinners for long-running tasks, but clear them when done.
