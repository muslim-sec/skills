---
name: debug-pro
description: Provides advanced tactical commands and memory management for traversing massive codebases during deep debugging sessions.
---

# Debug Pro

**Role:** Codebase Navigator
**Objective:** Prevent AI agents from getting lost or overwhelmed when tracing bugs across multiple files.

## Guidelines
- Avoid reading entire files. Use `grep` or AST parsers to locate specific functions.
- Maintain a "Call Stack Trace" in your memory. Write it out explicitly in your thoughts to avoid losing track of how data flows between files.
- If a bug spans more than 3 files, create a temporary `scratch/debug-map.md` file to map the connections before attempting a fix.
