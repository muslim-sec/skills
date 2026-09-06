---
name: css-animation-skill
description: Baseline skill for configuring premium, fast CSS animations using Tailwind CSS v4 variables for a cohesive visual language.
version: 1.0.0
scope: ui-design
---

# Baseline CSS Animation Skill

*(Note: For advanced interactions, defer to `svelte5_animation_skill.md`. This file governs the baseline CSS utilities.)*

## 1. The Premium Motion Guidelines
*   **Speed:** UI should feel "fast as f***". Hover transitions should use duration classes like `duration-150` or `duration-200`. Never exceed 300ms for simple state changes.
*   **Subtlety:** Do not use aggressive transformations unless requested. A premium button hover involves a subtle color shift and a tiny scale (`scale-105` down to `active:scale-95`).

## 2. Core Tailwind Tokens
Establish global CSS variables in `app.css` mapped to Tailwind `@theme`:
```css
@theme {
  --ease-fluid: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## 3. Hover Effects
*   Always chain `transition-colors`, `transition-transform`, and `transition-opacity` where applicable to avoid jerky pixel snaps.

## 4. Loading States
*   Instead of static blocks, use a subtle `animate-pulse` mixed with a gradient sweep (skeleton loading) to make waiting feel organic.
