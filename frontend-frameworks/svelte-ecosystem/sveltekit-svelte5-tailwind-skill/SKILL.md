---
name: sveltekit-svelte5-tailwind-skill
description: Comprehensive integration skill for building sites with SvelteKit 2, Svelte 5, and Tailwind CSS v4.
version: 1.0.0
scope: integration
---

# SvelteKit 2 + Svelte 5 + Tailwind v4 Skill

## 1. Core Stack
*   **Svelte 5 Runes:** Use `$state`, `$derived`, and `$effect` for reactive logic instead of `export let`.
*   **Tailwind v4:** Uses the new `@theme` configuration purely in CSS. No `tailwind.config.js` required.

## 2. Component Design
*   Build encapsulated logic blocks. Pass data in via `let { ... } = $props()`.
*   Avoid inline `<style>` blocks when possible; rely strictly on Tailwind utility classes for consistency and CSS Custom Properties for theme tokens.

## 3. UI Aesthetics (Glassmorphism & Cyberpunk)
*   Use `backdrop-blur` utilities to create frosted glass effects.
*   Implement high-contrast glowing elements (like `hud-glow`) using box-shadows and SVG stroke techniques.

## 4. Directory Structure
*   `src/lib/components/ui/` for dumb, reusable atoms (TaskCard, Button).
*   `src/lib/components/layout/` for structural components (Header, Sidebar).
*   `src/routes/` for SvelteKit page mapping and layout wrappers.
