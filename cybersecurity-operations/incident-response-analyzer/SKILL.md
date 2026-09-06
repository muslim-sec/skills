---
name: Log & Incident Analyzer
description: Analyzes server logs, access logs, and system events to detect anomalies, indicators of compromise (IoCs), and potential breaches.
---

# Incident Response Analyzer

Use this skill when the user provides log files (e.g., Apache/Nginx access logs, Linux auth.log, AWS CloudTrail) and wants to investigate suspicious activity.

## Capabilities
- **Anomaly Detection**: Look for rapid failed login attempts (Brute Force), unusual geographical access, or suspicious HTTP methods.
- **IoC Extraction**: Extract malicious IP addresses, User-Agents, or payload signatures (e.g., SQLi strings in URLs).
- **Attack Reconstruction**: Build a timeline of the attacker's actions based on log timestamps.

## Guidelines
1. Read the provided log snippets carefully.
2. Group related suspicious events to form an attack narrative.
3. Provide actionable remediation steps (e.g., "Block IP X", "Rotate credentials for User Y", "Patch vulnerability Z").
