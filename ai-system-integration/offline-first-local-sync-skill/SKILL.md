---
name: offline-first-local-sync-skill
description: Comprehensive architecture skill for Offline-First and Local Database Synchronization in Svelte 5 and Supabase.
version: 1.0.0
scope: integration
---

# Offline-First & Local Database Sync Skill

This guide outlines the architectural design for building a local-first Second Brain application.

## 1. Architectural Philosophy
All read/write actions occur **locally first**, updating the UI instantly, and sync with the cloud (Supabase) in the background. No loading spinners.

## 2. Web Implementation Stack
Use **Dexie.js** to manage IndexedDB queries in Svelte 5.
Tables: `tasks`, `projects`, `goals`, `sync_queue`.

## 3. The Sync Wrapper (Svelte 5 Runes)
Create a class that uses `$state` to hold local data arrays.
*   **Write Flow:** UI Action -> Push to $state -> Write to Dexie -> Add to Dexie `sync_queue` -> Trigger background upload to Supabase.
*   **Conflict Resolution:** Last-Write-Wins based on `updated_at` timestamps. Soft deletes (`deleted: 1`) only.

## 4. Desktop Integration (Tauri v2)
For Tauri desktop apps, the logic remains identical, but the Dexie.js wrapper is swapped for a Tauri SQLite plugin to interact directly with the OS filesystem.
