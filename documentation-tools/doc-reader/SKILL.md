---
name: doc-reader
description: >-
  Reads external documentation (via URL, Markdown file, or pasted text) and acts as an interactive tutor. Automatically falls back to Exa Search if a URL is blocked, or requests manual input.
---

# Documentation Reader & Tutor

## Overview
This skill allows the agent to ingest documentation for an application, framework, or programming language and act as a personalized, interactive tutor. It is designed to handle web scraping failures gracefully and ensures responses are strictly based on the provided material.

## Dependencies
- `read_url_content` (Native tool for URL reading)
- `web_search_exa` (Fallback search tool)

## Quick Start
"Use the doc-reader skill to read this documentation URL [URL] and help me understand how the routing system works."

## Workflow

### 1. Ingest Documentation
- If the user provides a URL, use the `read_url_content` tool to fetch it.
- If the user provides a local file path or pasted text, read it directly.

### 2. Handle Ingestion Failures
- If the URL blocks automated scraping (e.g., 403 Forbidden, requires login, or CAPTCHA), automatically fallback to using `web_search_exa` to find a cached or alternative version of the documentation.
- If all automated attempts fail, **pause** and ask the user to manually copy-paste the text or download and provide the HTML file.

### 3. Comprehend and Tutor
- Once the documentation is successfully ingested, read it deeply to build context.
- Answer the user's questions, explain complex concepts, and provide guided examples based *strictly* on the ingested documentation.

### 4. Guardrails for Missing Context
- If the user asks a question that is not covered by the ingested documentation, **do not hallucinate or invent answers**.
- Explicitly state that the information is missing from the provided docs, and ask if the user would like you to perform a broader web search to find the answer.

## Rate Limiting
- Handled natively by the built-in MCPs and web tools.

## Common Mistakes
- **Hallucinating outside the docs:** Answering a question using general LLM knowledge instead of restricting answers to the provided documentation.
- **Failing silently on URLs:** Giving up on a bad URL without trying Exa Search or asking the user for manual text.
