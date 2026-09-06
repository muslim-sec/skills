---
name: python-chart-generator
description: >-
  The Charting Expert: Writes and executes Python code (matplotlib/seaborn/plotly) to generate beautiful, high-resolution aesthetic charts from data.
---

# Python Chart Generator

## Overview
This skill is purely technical. It takes data and a visual blueprint, writes Python code, executes it, and saves professional-grade images locally.

## Workflow
1. **Ingest Blueprint**: Receive instructions on what chart to build (e.g., Bar chart of vulnerabilities by host).
2. **Write Python Script**: 
   - Use `matplotlib`, `seaborn`, or `plotly`.
   - Apply a premium aesthetic (dark mode, specific hex colors for Critical/High/Med/Low, clean fonts, remove unnecessary gridlines).
3. **Execute & Save**: Run the script and save the output as a high-res PNG or SVG in the project's `assets/` directory.
4. **Verify**: Ensure the image was created successfully and return the local file path.

## Rules
- The Python code MUST save to a file (`plt.savefig()`), never attempt to display a GUI window (`plt.show()`).
- Always use a modern, clean styling configuration.
