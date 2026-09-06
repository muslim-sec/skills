---
name: ui-ux-design-audit-skill
description: A comprehensive framework for analyzing and auditing UI/UX design. Detects visual flaws, usability issues, and inconsistencies across web and desktop applications.
version: 1.0.0
scope: ui-ux-design
---

# UI/UX Design Audit Skill

This skill provides a systematic framework for deeply analyzing an application's design to detect flaws, inconsistencies, and areas that fail to meet "Premium" standards.

## 1. Visual Hierarchy & Structure
*   **The Squint Test:** If you squint your eyes, what is the most prominent element? Is it the primary Call to Action (CTA)?
*   **Alignment:** Are all elements perfectly aligned to a grid system? (Look for stray margins, misaligned icons).

## 2. Spacing & Whitespace (Negative Space)
*   **Breathing Room:** Do elements feel cramped? Premium designs use generous whitespace.
*   **Proximity Principle:** Are related items grouped closely together?
*   **Consistency:** Are margin and padding tokens (e.g., `gap-sm`, `p-md`) used consistently?

## 3. Typography Consistency
*   **Hierarchy:** Is there a clear distinction between `Headline`, `Sub-headline`, `Body`, and `Label`?
*   **Readability:** Is the line height sufficient? (Usually 1.5 for body text). 

## 4. Color, Contrast & Accessibility
*   **Contrast Ratio:** Does text meet the WCAG AA contrast ratio (4.5:1) against its background?
*   **Color Meaning:** Is red strictly used for errors/destructive actions? 

## 5. Interaction & Feedback (The "Feel")
*   **State Changes:** Do all interactive elements have clear `hover`, `active`, and `focus` states?
*   **Loading States:** Are there skeleton loaders or micro-animations instead of jarring full-page spinners?

## 6. Premium Polish (The "Wow" Factor)
*   **Micro-interactions:** Are standard CSS transitions upgraded to Spring physics?
*   **Depth & Elevation:** Are shadows, borders, and glassmorphism layered logically?
