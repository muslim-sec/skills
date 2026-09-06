---
name: svelte5-expert-animation-skill
description: Comprehensive guide for implementing premium, hardware-accelerated animations and micro-interactions in Svelte 5.
version: 1.0.0
scope: ui-design
---

# Svelte 5 Expert Animation Skill

Guidelines for making the application feel fluid, organic, and ultra-responsive.

## 1. Core Principles
1.  **Physics over Math:** Use Spring Physics over linear easing for natural movement.
2.  **Hardware Acceleration:** Only animate `transform` and `opacity`. Never animate layout properties like width or margin.
3.  **Speed:** Animations should be fast (200-300ms for entering, 150ms for exiting).

## 2. Tools in Svelte 5
*   `svelte/transition`: (`fade`, `fly`, `slide`, `scale`).
*   `svelte/animate`: (`flip`) for list reordering.
*   `svelte/motion`: (`Spring`, `Tween`) for micro-interactions and continuous values.

## 3. Implementation Patterns

### List Reordering (Cards)
Use `animate:flip` and `in:fly` for tasks entering the timeline so they smoothly push other elements down.

### Micro-Interactions
Use `import { Spring } from 'svelte/motion'` tied to `onpointerdown` events to give buttons tactile, squishy feedback.

### SVG Glows
Use `Tween` to smoothly interpolate SVG `stroke-dashoffset` for timers and progress rings instead of rigid CSS transitions.

### View Transitions
Utilize the native browser View Transitions API tied into SvelteKit's `onNavigate` hook to create seamless, Native-App-like page changes.
