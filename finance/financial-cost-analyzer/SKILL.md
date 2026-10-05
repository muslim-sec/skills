---
name: financial-cost-analyzer
description: >-
  Analyzes financial data, cloud billing (AWS/GCP), project budgets, and subscription costs. Identifies anomalies, calculates burn rates, and generates cost-optimization visualizations.
---

# Financial & Cost Data Analyzer

## Overview
This skill transforms the agent into a FinOps and Financial Analyst. It ingests billing reports, budgets, or raw financial CSVs to find where money is being wasted, forecast future costs, and present visual financial health dashboards.

## Workflow
1. **Ingest Financial Data**: Read CSVs, JSONs, or text exports of billing data, AWS Cost Explorer reports, or general budget sheets.
2. **Cost Normalization & Categorization**: Group costs by service, department, or project. Identify one-off spikes versus recurring operational expenses (OpEx).
3. **Anomaly & Waste Detection**: Calculate the month-over-month (MoM) change. Highlight any service that spiked anomalously or unused resources (e.g., unattached EBS volumes, idle servers).
4. **Forecasting (Burn Rate)**: Calculate the current burn rate and project when the budget will run out if spending continues at the current pace.
5. **Visualization Blueprint**: Generate instructions to create charts (e.g., "Stacked bar chart for monthly spend by category", "Line chart for projected burn rate") and pass them to the `python-chart-generator` skill.

## Rules
- Always format currency outputs clearly (e.g., $1,234.56).
- Do not make financial decisions for the user; only present the data, highlight the waste, and provide optimization recommendations.
