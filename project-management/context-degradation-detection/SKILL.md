---
name: context-degradation-detection
description: Monitors AI reasoning during long multi-step debugging tasks to prevent hallucination, loop-getting, and context amnesia.
---

# Context Degradation Detection

**Role:** Meta-Cognition Monitor
**Objective:** Recognize when you (the AI) are going in circles or forgetting earlier constraints.

## Detection Triggers
- You have proposed the same fix twice and it failed both times.
- The user tells you that a file you are referencing does not exist.
- You have executed more than 10 tool calls without resolving the core issue.

## Recovery Protocol
If degradation is detected:
1. **Halt execution.** Stop modifying code.
2. **Clear Context:** Summarize everything known to be true into a bulleted list.
3. **Ask for Help:** Present the summary to the user and explicitly ask them for a course correction or a fresh perspective.
