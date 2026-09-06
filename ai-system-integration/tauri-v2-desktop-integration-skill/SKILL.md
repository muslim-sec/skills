---
name: tauri-v2-desktop-integration-skill
description: Guidelines for compiling web applications into extremely fast, offline-first desktop apps using Tauri v2.
version: 1.0.0
scope: desktop-integration
---

# Tauri v2 Desktop Integration Skill

## 1. Architecture Overview
Tauri wraps your SvelteKit frontend in a lightweight OS webview (WebKit/WebView2) and uses a Rust backend to handle system-level access. It results in binary sizes <10MB and near-zero RAM overhead compared to Electron.

## 2. Setup Rules
*   SvelteKit MUST use `@sveltejs/adapter-static` with `ssr = false` to pre-render the app into HTML/JS files that Tauri can consume.
*   Tauri configuration (`tauri.conf.json`) handles window sizes, transparency, and permissions.

## 3. Advanced Features
*   **System Tray / Menu Bar:** Enable a quick-access menu bar widget for logging tasks without opening the full app.
*   **Global Shortcuts:** Register OS-level shortcuts (e.g., `Cmd+Shift+Space`) to instantly bring up the "New Thought" entry modal.
*   **Local File Access:** Bypass standard browser security sandboxes to read/write files directly to the user's hard drive using Tauri APIs.
