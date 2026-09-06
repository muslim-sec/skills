---
name: local-ai-ollama-integration-skill
description: Framework for integrating offline, local Large Language Models (LLMs) via Ollama into the application for zero-latency, private AI assistance.
version: 1.0.0
scope: ai-integration
---

# Local AI & Ollama Integration Skill

## 1. Core Philosophy (100% Privacy)
A "Second Brain" contains intimate, private thoughts. By leveraging Ollama to run models (like Llama 3 or Phi-3) locally on the user's hardware, no data is ever sent to external cloud APIs like OpenAI.

## 2. Integration Mechanics
*   **API Protocol:** The SvelteKit app communicates directly with the local Ollama API (usually running on `http://localhost:11434/api/generate`).
*   **Streaming Responses:** Use HTTP streaming logic to render AI responses word-by-word instantly, ensuring the UI remains highly responsive.

## 3. Features
*   **Auto-Tagging:** Automatically read local task/note inputs and suggest tags or areas without prompting.
*   **Semantic Search (RAG):** Use a local embedding model (e.g., `nomic-embed-text`) stored in a pgvector Supabase schema or local vector database to find related notes instantly.
*   **Critic Mode:** Actively monitor input in a floating window and provide context-aware suggestions while typing.
