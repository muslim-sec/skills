---
name: security-data-analyst
description: >-
  The Reasoning Brain: Analyzes aggregated pentest data to identify trends, attack vectors, and risk clusters. Calculates statistics and forms logical conclusions.
---

# Security Data Analyst

## Overview
This skill takes clean, normalized data (usually from `pentest-data-ingestor`) and applies analytical reasoning. It looks for the "story" behind the data rather than just listing vulnerabilities.

## Workflow
1. **Statistical Analysis**: Calculate totals, percentages, and severities (e.g., "40% of criticals are related to outdated SSL"). Use Python scripts (`pandas`) if the dataset is large.
2. **Trend Identification**: Group vulnerabilities by subnet, application, or vulnerability class (OWASP Top 10).
3. **Attack Path Modeling**: Identify if multiple low/medium vulnerabilities can be chained together to form a critical attack vector.
4. **Insight Generation**: Produce a written analytical summary of the highest risks, anomalous data points, and systemic issues found in the network.

## Rules
- Focus on the "Why" and "How", not just the "What".
- Always support claims with data statistics extracted from the source files.
