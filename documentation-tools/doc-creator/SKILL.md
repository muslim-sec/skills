---
name: doc-creator
description: >-
  Generates production-ready Docusaurus v3 documentation. Scaffolds hierarchical MD/MDX files with correct frontmatter and sidebar logic, adhering to project branding. Strictly pauses if critical technical context is missing.
---

# Professional Docusaurus Documentation Creator

## Overview
This skill transforms source code, project descriptions, or raw notes into a professional, website-ready documentation structure specifically tailored for Docusaurus v3. It strictly enforces an anti-hallucination policy to ensure absolute technical accuracy.

## Dependencies
- `write_to_file` (Native tool for creating Markdown files)
- `grep_search` / `find` (Native tools for scanning project directories)

## Quick Start
"Use the doc-creator skill to generate professional Docusaurus documentation for my new authentication module."

## Workflow

### 1. Analyze Project Context & Branding
- Before writing, briefly scan the project workspace for existing Docusaurus configurations (`docusaurus.config.js`), custom CSS, or company branding guidelines.
- If specific styles or configurations are found, strictly adhere to them. If none exist, default to standard Docusaurus v3 conventions.

### 2. Scaffold Docusaurus Structure
- Plan a logical, hierarchical documentation structure suitable for a sidebar navigation system (e.g., Introduction, Installation, Configuration, Features, Guides, API Reference, Troubleshooting).
- Use the `write_to_file` tool to scaffold the necessary `docs/` folder and individual `.md` or `.mdx` files.

### 3. Generate Content & Frontmatter
- Write professional, production-ready content for each file.
- Ensure every Markdown file contains valid Docusaurus YAML frontmatter at the top (e.g., `id`, `title`, `sidebar_position`).
- Use advanced Markdown/MDX features (like Admonitions/Callouts) where appropriate to make the documentation visually appealing.

### 4. Strict Anti-Hallucination Guardrails
- If critical technical details (such as API endpoints, exact configuration flags, or specific application behaviors) are missing from the source material, **PAUSE** and explicitly ask the user for clarification.
- **NEVER** invent facts, APIs, configuration options, behavior, or technical details.

### 5. Handle Minor Gaps
- For minor or non-critical gaps, you may proceed using only information that can be reliably inferred.
- Any assumptions made during this process must be clearly flagged (e.g., using a warning admonition or a Markdown comment) so the user can easily review and correct them later.

## Rate Limiting
- N/A (Local file generation only).

## Common Mistakes
- **Writing generic Markdown:** Failing to include Docusaurus frontmatter (`title`, `sidebar_position`) or ignoring the sidebar hierarchy.
- **Hallucinating technical details:** Inventing API parameters or configuration flags to make the documentation look "complete" when the source code doesn't provide them.
