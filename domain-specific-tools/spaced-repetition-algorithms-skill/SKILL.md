---
name: spaced-repetition-algorithms-skill
description: Guidelines for implementing scientifically proven Active Recall and Spaced Repetition systems (SM-2, FSRS) within a Second Brain app.
version: 1.0.0
scope: learning-algorithms
---

# Active Learning & Spaced Repetition Skill

## 1. Concept: Learn How to Learn
Information stored but never reviewed is forgotten. The app must implement algorithms to surface notes and flashcards just before the user is likely to forget them.

## 2. Algorithm Choices
*   **SM-2 (SuperMemo-2):** The classic, reliable algorithm based on ease factor, interval, and repetitions. Easy to implement in Javascript.
*   **FSRS (Free Spaced Repetition Scheduler):** A modern, machine-learning-based algorithm that optimizes review schedules far better than SM-2.

## 3. Implementation
*   **Data Structure:** Each flashcard or note block must track `last_review_date`, `next_review_date`, `interval`, and `ease_factor`.
*   **UI Workflow:** 
    1. Show Question.
    2. User mentally recalls answer.
    3. Click "Show Answer".
    4. User rates difficulty (Again, Hard, Good, Easy).
    5. Algorithm calculates and updates the `next_review_date` in the Dexie.js local database.
