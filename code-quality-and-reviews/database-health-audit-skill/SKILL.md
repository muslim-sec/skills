---
name: database-health-audit-skill
description: A comprehensive framework for verifying database integrity, synchronization health, and enforcing backup/disaster recovery strategies.
version: 1.0.0
scope: database-reliability
---

# Database Health & Backup Audit Skill

This skill provides a systematic framework to guarantee that the application's data is safe, uncorrupted, and properly backed up.

## 1. Local Database Integrity (Dexie.js / IndexedDB)
*   **Corruption Checks:** Are there `try/catch` blocks around local database reads/writes? 
*   **Orphaned Data:** Are there records pointing to deleted parent IDs?

## 2. Synchronization Health (The Sync Queue)
*   **Queue Bottlenecks:** Is the `sync_queue` piling up without resolving? 
*   **Last-Write-Wins Verification:** Is the `updated_at` timestamp strictly enforced in both local and cloud databases?
*   **Tombstone Management:** Are soft-deleted items properly managed before final purge?

## 3. Cloud Database Integrity (Supabase)
*   **Row-Level Security (RLS):** Are all tables protected by strict RLS policies ensuring users only access their own data?
*   **Referential Integrity:** Does the SQL schema enforce `ON DELETE CASCADE`?

## 4. Backup Strategies (Zero Data Loss)
*   **Local Backup (Manual Export):** The app must provide a "Download My Brain" feature exporting all data to JSON.
*   **Cloud Backup (Automated):** Supabase Point-in-Time Recovery (PITR) or scheduled `pg_dump` jobs for cold storage.

## 5. Disaster Recovery (Restore Protocol)
*   **Wipe & Re-sync:** A "Factory Reset" feature to clear local corruption and pull fresh from cloud.
*   **JSON Import:** A feature to safely upsert from a manual JSON backup.
