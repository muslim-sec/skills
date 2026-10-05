# TestSprite (functional & access-control testing)

TestSprite reads the codebase and a PRD, generates test plans, and drives the running app like real users in cloud sandboxes, returning failures with screenshots, root-cause hypotheses, and fix suggestions. In this skill it covers what scanners can't: broken login flows, role/permission logic, and cross-user data access.

Docs: https://docs.testsprite.com/web-portal/getting-started/overview · MCP: https://docs.testsprite.com/mcp/getting-started/installation

## 1. Check whether it's available
Look for MCP tools whose names contain `testsprite` (e.g. `testsprite_bootstrap`). If present, call a harmless one first (bootstrap with the correct port) to confirm the API key works.

## 2. Help the user set it up (if missing)
Requirements: Node.js ≥ 22, a TestSprite account, an API key from the TestSprite dashboard (Settings → API Keys).

Generic MCP config (Cursor, Windsurf, VS Code, Trae, etc.):
```json
{
  "mcpServers": {
    "TestSprite": {
      "command": "npx",
      "args": ["@testsprite/testsprite-mcp@latest"],
      "env": { "API_KEY": "<your-testsprite-api-key>" }
    }
  }
}
```
Claude Code:
```bash
claude mcp add TestSprite --env API_KEY=<your-key> -- npx @testsprite/testsprite-mcp@latest
```
Ask the user to paste the key into their own config rather than into chat. After setup the client usually needs a restart/reload for the tools to appear. Verify with `node -v` (≥22) and by checking the tool list again.

If MCP isn't possible (e.g. no local runtime), the **web portal** works against a deployed URL: create a UI or API project, give it the staging URL and test credentials, and let it explore, plan, and run. Import the results into the findings list manually.

## 3. Workflow (MCP)
Tool names as documented (confirm against the live tool list — they may evolve):
1. Start the app locally (`npm run dev` / `npm run build && npm start`) and note the port.
2. `testsprite_bootstrap` — `localPort`, `type` (`frontend` or `backend`), `projectPath` (absolute), `testScope` (`codebase` or `diff`).
3. `testsprite_generate_code_summary` → `code_summary.json`.
4. `testsprite_generate_standardized_prd` → `standard_prd.json`. If the user has a real PRD, give it to TestSprite instead — better tests.
5. `testsprite_generate_frontend_test_plan` (`needLogin`) and/or `testsprite_generate_backend_test_plan`.
6. `testsprite_generate_code_and_execute` — use `additionalInstruction` to focus on security-relevant behavior (below).
Outputs: `testsprite_tests/` with `TestSprite_MCP_Test_Report.md/.html` and `tmp/test_results.json`.

## 4. Security-focused test instructions
Provide **dedicated test accounts** (never real user credentials), ideally on staging: at least two regular users (A, B) and one admin if roles exist. Suggested `additionalInstruction` themes:
- Unauthenticated visitors are redirected from every protected page and API returns 401/403.
- User A cannot view, edit, or delete User B's records via UI or API (IDs from B's session).
- Non-admin users get 403 on admin pages and admin API routes.
- Logout invalidates the session; expired sessions can't be reused.
- Forms reject invalid/oversized input with a validation message, not a 500.
- Password reset/magic links work once and expire.

## 5. Importing results
Each failed test that relates to auth, authz, sessions, or input handling becomes a finding (`SEC-AUTHZ-*`, `SEC-AUTH-*`, `SEC-INPUT-*`) with the test ID, failing step, and TestSprite's root-cause hypothesis as evidence. Pure functional bugs go into an appendix "Non-security defects found". Re-run the failing tests after fixes (`testIds`) for verification.
