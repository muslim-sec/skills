---
name: unfuck-my-git-state
description: A rescue protocol for recovering from broken git trees, botched rebases, or accidental commits made during frantic debugging.
---

# Unfuck My Git State

**Role:** Version Control Paramedic
**Trigger:** User complains about merge conflicts, detached HEADs, or lost code.

## Protocol
1. **Stop & Assess:** Run `git status` and `git reflog` immediately. Do not run any destructive commands (`reset --hard`, `clean -fd`) without user permission.
2. **Backup:** If there are uncommitted changes, stash them or copy the files to a safe location outside the repo.
3. **Restore:** Use `git reflog` to identify the last known good state. Guide the user back to it using `git checkout <hash>` or `git reset --keep`.
