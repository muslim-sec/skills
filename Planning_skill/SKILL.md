---
name: Planning_skill
description: >
  ⭐ Enforces a structured, detailed planning workflow for any coding task.
  Ensures every plan clearly defines its purpose (bug fix, new feature, feature extension),
  resolves all file paths during planning, describes changes in detail, includes a verification
  strategy, and produces a ready-to-execute task list. Activate this skill whenever you are
  asked to create a plan, implementation plan, or any task that requires planning before execution.
---

# Precise Planning Skill

## Core Philosophy

> **Planning is for Discovery. Execution is for Action.**

All research, searching, path resolution, and decision-making MUST happen during planning.
The execution phase should be a deterministic, step-by-step execution of well-defined tasks
with **zero** discovery or searching required.

---

## Phase 1: Define the Purpose

Every plan MUST begin with a clear **Purpose Statement**. Before writing anything else,
classify the task into one of these categories and state it explicitly at the top of the plan:

| Purpose Type | When to Use | Example |
|---|---|---|
| 🐛 **Bug Fix** | Something is broken or behaving incorrectly | "Fix: Login form submits empty data when password field is autofilled" |
| ✨ **New Feature** | Building something that doesn't exist yet | "New Feature: Add dark mode toggle to settings page" |
| 🔧 **Feature Extension** | Adding capability to an existing feature | "Extend: Add CSV export option to the existing reports page" |
| ♻️ **Refactor** | Restructuring code without changing behavior | "Refactor: Extract authentication logic into a shared middleware" |
| ⚡ **Performance Fix** | Improving speed, memory, or efficiency | "Performance: Optimize database queries on the dashboard page" |
| 🔒 **Security Fix** | Addressing a vulnerability or hardening security | "Security: Sanitize user input on the comment submission endpoint" |

### Purpose Statement Format

```markdown
## Purpose

**Type:** 🐛 Bug Fix
**Summary:** [One-line description of what this plan accomplishes]
**Context:** [Why this change is needed — the problem, the user report, or the goal]
**Expected Outcome:** [What success looks like when this plan is fully executed]
```

---

## Phase 2: Research & Discovery

This is where ALL searching, reading, and exploring happens. You MUST complete this phase
before writing the plan.

### 2.0 — Read Project Context Files (Mandatory First Step)

Before doing ANY other research, you MUST locate and read the project's configuration and
context files. These files contain critical rules, conventions, architecture decisions, and
constraints that govern how code should be written in this project.

**Search for and read ALL of the following files if they exist:**

| File | Purpose |
|---|---|
| `.cursorrules` or `.cursor/rules/` | Project rules for Cursor AI |
| `.github/copilot-instructions.md` | GitHub Copilot instructions |
| `gemini.md`, `claude.md`, `agent.md` | Core AI instructions and global behavior rules |
| `ARCHITECTURE.md` or `docs/architecture.md` | Architecture documentation |
| `CONTRIBUTING.md` | Contribution guidelines and conventions |
| `.editorconfig` | Editor configuration and code style rules |
| `.eslintrc.*` / `biome.json` / `prettier.config.*` | Code style and linting rules |
| `tsconfig.json` / `jsconfig.json` | TypeScript/JavaScript configuration |
| `package.json` | Dependencies, scripts, and project metadata |
| `README.md` | Project overview and setup instructions |
| Any `.rules`, `.agent`, `.ai`, or `.gemini` files | Agent-specific instructions |

**Why this matters:**
- These files define the project's coding standards, naming conventions, and architectural patterns.
- Ignoring them leads to plans that violate project rules, requiring costly rework.
- Reading them FIRST ensures your plan aligns with the project from the start.
- The architecture docs tell you what patterns to follow, what libraries are used, and where things belong.

**Rule:** If you cannot find any project context files, explicitly state this in your plan
and ask the user if there are any project conventions you should follow before proceeding.

### Rules

1. **Use your tools NOW** — Run `list_dir`, `grep_search`, `view_file`, and any other
   research tools to locate every file, folder, function, and dependency relevant to the task.
2. **Generate Options & Challenge the Idea** — Before deciding on the final approach, explicitly generate 2-3 different ways to solve the problem. Challenge these ideas to find weaknesses, and select the optimal approach. Do this *before* writing the detailed plan.
3. **Resolve absolute paths** — Every file or directory you discover MUST be recorded with
   its full absolute path (e.g., `/Users/username/project/src/components/Button.tsx`).
   **NEVER** use floating names like "the components folder" or "app.js".
3. **Verify existence** — Do not assume any file or folder exists. Confirm with tools first.
   If a file will be created, verify that the parent directory exists.
4. **Identify exact locations** — For files that will be modified, identify the exact line
   numbers, function names, or code blocks that need changes. Document them.
5. **Map dependencies** — Identify what other files import, call, or depend on the files
   you plan to change. Document the dependency chain so you don't break anything.

### Research Checklist

Before moving to Phase 3, confirm you have:

- [ ] Read all available project context and configuration files
- [ ] Generated 2-3 alternative approaches and selected the optimal one
- [ ] Mapped the blast radius: Identified all existing features and functions that might be broken by this new change.
- [ ] Located all files to be modified (with absolute paths)
- [ ] Located all files to be created (with absolute paths of parent directories)
- [ ] Identified exact line numbers or functions to change
- [ ] Mapped imports and dependencies that could be affected
- [ ] Checked for existing tests related to the changed code
- [ ] Reviewed any relevant configuration files

---

## Phase 3: Write the Detailed Plan

The plan document (`implementation_plan.md`) MUST follow this structure:

### 3.1 — Purpose (from Phase 1)

State the purpose type, summary, context, and expected outcome.

### 3.2 — Proposed Changes (Detailed)

Group changes by component or feature area. For each file, describe **exactly** what changes
and why.

#### Format for Modified Files

```markdown
### [Component Name]

#### [MODIFY] [filename.ext](file:///absolute/path/to/file.ext)

**What changes:**
- Add input validation to the `handleSubmit()` function (lines 45-62)
- Add a new `validateEmail()` helper function after line 80
- Update the error state to include field-level errors (line 23)

**Why:**
- The form currently submits without validating required fields, causing server-side 400 errors

**Dependencies affected:**
- [UserForm.test.js](file:///absolute/path/to/UserForm.test.js) — tests will need updating
- [api.js](file:///absolute/path/to/api.js) — no changes needed, already handles validation errors
```

#### Format for New Files

```markdown
#### [NEW] [filename.ext](file:///absolute/path/to/new/file.ext)

**Purpose:** Describe what this file does and why it's needed
**Contents:** Brief description of the file's structure (exports, functions, classes)
**Used by:** List which existing files will import or use this new file
```

#### Format for Deleted Files

```markdown
#### [DELETE] [filename.ext](file:///absolute/path/to/file.ext)

**Reason:** Why this file is being removed
**Migration:** Where its functionality has moved to (if applicable)
**Dependents:** List files that currently import this file and how they will be updated
```

### 3.3 — Actionable File Links

Every single file mentioned in the plan MUST use clickable Markdown links:

- ✅ **Good:** `[Button.tsx](file:///Users/mac/project/src/components/Button.tsx)`
- ✅ **Good:** `[Button.tsx](file:///Users/mac/project/src/components/Button.tsx#L45-L62)`
- ❌ **Bad:** `Button.tsx`
- ❌ **Bad:** `src/components/Button.tsx`
- ❌ **Bad:** "the Button component"

### 3.4 — Open Questions & Decisions

If there are design decisions or ambiguities, list them clearly using alerts:

```markdown
> [!IMPORTANT]
> Should we use client-side or server-side validation? Client-side gives better UX
> but server-side is more secure. Recommend: both.

> [!WARNING]
> This change will modify the API response shape. Any frontend consumers will need updating.
```

### 3.5 — Impact Analysis (Regression Risks)

Whenever you are planning to add a new feature or modify existing logic, you MUST explicitly identify all currently working features, functions, or shared components that might be affected by this change. 

```markdown
### Impact Analysis
- **Affected Features:** (e.g., User Authentication, Checkout Flow, Profile Settings).
- **Shared Components/Functions:** (e.g., Modifying the `formatDate` utility might affect the Dashboard views).
- **Regression Testing Required:** All features listed here MUST be explicitly included in the Verification Plan (Phase 5) to guarantee they still work perfectly after the new changes are executed.
```

### 3.6 — Execution Strategy Recommendation

Provide explicit recommendations on how this plan should be executed:

```markdown
### Execution Recommendation
- **Suggested Model:** (e.g., Flash for simple, highly detailed tasks; Pro for complex architectural execution).
- **Thinking Density:** Specify the required intensity of reasoning (Low, Medium, High, Max) based on the risk and complexity of the task.
- **Required Sub-Agents:** Explicitly list any specialized sub-agents needed to execute this plan (e.g., Senior Software Developer, UI/UX Designer, QA Specialist) based on the user's prompt or task requirements.
- **Environment:** (e.g., Recommend using a Git Worktree to avoid conflicts if working on a large parallel feature).
- **Pattern:** (e.g., Direct execution vs. Orchestrator-Worker pattern with sub-agents).
```

---

## Phase 4: Adversarial Plan Review (Devil's Advocate)

**The plan MUST NOT be presented to the user until it passes this review.**

Before showing your plan to the user, you MUST delegate it to a separate reasoning pass
(a subagent, a second model call, or an internal adversarial review) that acts as a
**Devil's Advocate**. The goal is to ensure the plan is the **best possible solution**
from the first attempt — zero millimeters of mistake.

### How It Works

1. **Spawn three dynamic sub-agents** — Spawn and coordinate three independent sub-agents to review and criticize the proposed plan and app architecture. **Their roles MUST be dynamic based on the task Purpose.** For example:
   - For a ⚡ **Performance Fix**: Spawn a Performance Expert, an Architect, and a QA Specialist.
   - For a 🎨 **UI/UX Update**: Spawn an Accessibility/UI Expert, a Frontend Architect, and a QA Specialist.
   - For a 🔒 **Security Fix**: Spawn a Penetration Tester, a Security Architect, and a QA Specialist.
2. **Analyze & Criticize** — Each of the three sub-agents must independently audit the plan to identify structural flaws, security gaps, performance bottlenecks, or unhandled edge cases.
3. **Update & Fix Weakness Points** — If any of the three sub-agents identify a weakness point, you must update the implementation plan, apply the fixes, and repeat the review cycle until all three sub-agents approve.
4. **The reviewers' mandate** — The reviewers MUST ruthlessly attempt to:

   | Review Dimension | What the Reviewer Checks |
   |---|---|
   | **Architecture** | Is this the right pattern? The right abstraction level? Is there a simpler, cleaner approach? |
   | **Completeness** | Are there missing steps, unhandled edge cases, or forgotten error scenarios? |
   | **Project Alignment** | Does the plan follow the conventions and rules discovered in the project context files? |
   | **Complexity** | Is there unnecessary over-engineering? Could any part be simplified? |
   | **Correctness** | Will this actually work on the first implementation attempt? Any race conditions or logical errors? |
   | **Security** | Are there unaddressed security concerns (injection, auth bypass, data exposure)? |
   | **Performance** | Will this introduce performance regressions? Any N+1 queries, memory leaks, or blocking calls? |
   | **Dependencies** | Will this break existing functionality? Are all affected files accounted for? |
   | **Better Alternatives** | Is there a fundamentally better solution the plan didn't consider? |

3. **Produce a verdict** — The reviewer produces one of three outcomes:

   | Verdict | Meaning | Action |
   |---|---|---|
   | ✅ **APPROVED** | Plan is solid, no significant issues found | Proceed to present the plan to the user |
   | 🔧 **REVISE** | Issues found but the approach is sound | Fix the issues in the plan, then re-review |
   | 🚫 **REJECT** | Fundamental approach is wrong, a better solution exists | Rewrite the plan with the better approach, then re-review |

### Review Prompt Template

When delegating the adversarial review, use this prompt:

```
You are a senior software architect and Devil's Advocate. Your SOLE job is to find every
possible flaw, inefficiency, and missed opportunity in the following implementation plan.
Be ruthless. Be thorough. Be constructive.

**Project Context & Rules:**
[Paste the project rules, conventions, and architecture constraints discovered in Phase 2]

**The Implementation Plan:**
[Paste the complete plan from Phase 3]

**You MUST answer ALL of these questions:**
1. Is this the BEST architectural approach, or is there a fundamentally better solution?
2. Are there edge cases, error scenarios, or race conditions not handled?
3. Does this plan follow the project's conventions, patterns, and rules?
4. Is there unnecessary complexity that could be simplified?
5. Will this plan work correctly on the FIRST implementation attempt with zero rework?
6. Are the file paths, line numbers, and dependency mappings accurate?
7. Are there security, performance, or scalability concerns not addressed?
8. Is the verification plan thorough enough to catch ALL regressions?
9. What is the single biggest risk in this plan?

**Your Output MUST be:**
- **Verdict:** APPROVED | REVISE | REJECT
- **Confidence:** (1-10) How confident are you this plan will succeed on the first attempt?
- **Findings:** Numbered list of every issue found, ordered by severity
- **Recommendations:** For each finding, provide a specific, actionable fix
- **Alternative Approach:** (Only if REJECT) Describe the better solution in detail
```

### Rules

- Maximum **3 review cycles**. If the plan hasn't converged after 3 cycles, present the
  best version along with the unresolved concerns to the user for their decision.
- The review findings MUST be briefly summarized in the final plan under a
  **"🔍 Review Notes"** section, so the user can see the plan was stress-tested.
- If the reviewer suggests a fundamentally better approach, you MUST seriously consider it
  and explain to the user why you chose or rejected the alternative.

---

## Phase 5: Verification Plan

Every plan MUST include a verification strategy. This is NOT optional. The verification plan
has two parts:

### 5.1 — Automated Verification

List the exact commands to run after execution. **If the feature involves the UI, strongly recommend writing and running End-to-End (E2E) tests (e.g., Playwright, Cypress) to verify the feature from the user's perspective.**

```markdown
## Verification Plan

### Automated Tests
- `npm test -- --testPathPattern="UserForm"` — Run unit tests for the modified component
- `npm run lint` — Ensure no linting errors introduced
- `npm run build` — Verify the project builds successfully
- `npx playwright test login.spec.ts` — Run end-to-end UI tests to simulate real user interactions
```

### 5.2 — Manual Verification

Describe what the user should check visually or interactively:

```markdown
### Manual Verification
- [ ] Open the login page and submit with empty fields → should show validation errors
- [ ] Submit with valid data → should redirect to dashboard
- [ ] Check browser console for any JavaScript errors
- [ ] Test on mobile viewport (375px width) to ensure responsive layout
```

### 5.3 — Post-Verification Error Check

After running all tests:

```markdown
### Post-Verification
- [ ] All automated tests pass with zero failures
- [ ] No new lint warnings or errors
- [ ] Build completes successfully with no size regressions
- [ ] Manual verification items all confirmed working
- [ ] No regressions in related features (list them)
```

---

## Phase 6: Task List (`task.md`)

After the plan is approved, generate a task list that serves as the execution checklist.
Every task MUST include the absolute file path.

### Format

```markdown
# Task List

## Setup
- [ ] Create branch `fix/login-validation` from `main`

## Implementation
- [ ] Add `validateEmail()` to [validation.ts](file:///Users/mac/project/src/utils/validation.ts)
- [ ] Update `handleSubmit()` in [LoginForm.tsx](file:///Users/mac/project/src/components/LoginForm.tsx#L45-L62)
- [ ] Add error display in [LoginForm.tsx](file:///Users/mac/project/src/components/LoginForm.tsx#L23)

## Tests
- [ ] Update [LoginForm.test.tsx](file:///Users/mac/project/src/components/LoginForm.test.tsx) with validation test cases
- [ ] Add [validation.test.ts](file:///Users/mac/project/src/utils/validation.test.ts) for the new helper

## Verification
- [ ] Run `npm test` — all tests pass
- [ ] Run `npm run build` — builds successfully
- [ ] Manual: test empty form submission
- [ ] Manual: test valid form submission
```

### Task Rules

- ❌ **Bad:** `[ ] Update the user controller to add validation.`
- ✅ **Good:** `[ ] Add input validation to [user_controller.js](file:///Users/mac/backend/controllers/user_controller.js#L34-L50)`
- Mark tasks as `[/]` when in progress, `[x]` when done.
- Update `task.md` continuously during execution.

---

## Phase 7: Post-Execution Code Review

The job is not done when the code works. After verification, you MUST review the final code to ensure it meets quality standards and edge cases are handled. Add this final checklist to the `task.md`:

```markdown
## Phase 7: Post-Execution Review
- [ ] Architecture alignment: Ensure no new/rogue architectural patterns were invented.
- [ ] Edge cases: Review the code for unhandled rare states or logical gaps.
- [ ] Code cleanliness: Check for DRY violations, deep nesting, and tight coupling.
- [ ] Security: Verify no new vulnerabilities were introduced.
```

---

## Summary: The Planning Workflow

```
┌─────────────────────────────────────────────────┐
│  Phase 1: DEFINE PURPOSE                        │
│  What type of change? Why? Expected outcome?    │
├─────────────────────────────────────────────────┤
│  Phase 2: RESEARCH & DISCOVER                   │
│  Read project context files FIRST               │
│  Search files, resolve paths, map dependencies  │
│  ALL discovery happens HERE — not later         │
├─────────────────────────────────────────────────┤
│  Phase 3: WRITE DETAILED PLAN                   │
│  Exact changes per file, with paths & line nums │
├─────────────────────────────────────────────────┤
│  Phase 4: ADVERSARIAL REVIEW (Devil's Advocate) │
│  Stress-test the plan for flaws & alternatives  │
│  APPROVED → continue | REVISE → fix & re-review │
├─────────────────────────────────────────────────┤
│  Phase 5: VERIFICATION PLAN                     │
│  Automated tests + Manual checks + Error check  │
├─────────────────────────────────────────────────┤
│  Phase 6: TASK LIST                             │
│  Actionable checklist with absolute paths       │
│  Execute deterministically — zero searching     │
├─────────────────────────────────────────────────┤
│  Phase 7: POST-EXECUTION REVIEW                 │
│  Check architecture, edge cases, and code clean │
└─────────────────────────────────────────────────┘
```

## Critical Reminders

1. **Read the project first** — Always read project context/rules files before planning.
2. **No floating names** — Every file gets an absolute path. No exceptions.
3. **No searching during execution** — If you need to search, your plan was incomplete. Go back and fix it.
4. **Always review adversarially** — No plan reaches the user without being stress-tested.
5. **Always verify** — No plan is complete without a verification strategy.
6. **Purpose first** — Always classify the task before planning it.
7. **Show the diff** — Describe what changes in each file specifically, not vaguely.


## Pre-Planning Phase (Mandatory)
Before generating any plan or taking any action, you MUST invoke the `grill-me` skill. Do not write a single line of the plan until you have thoroughly interrogated the user about their feature, identified edge cases, and questioned their design choices. Only proceed to the actual planning phase once the `grill-me` interrogation has yielded an absolute, crystal-clear understanding of the requirements.



## Markdown Management (Mandatory for MD files)
If the plan involves generating, updating, or dealing with large Markdown (MD) files, you MUST invoke the `bmad-shard-doc` skill. This ensures that large documentation is properly sharded, structured, and split into manageable files to preserve context token limits and maintain top quality.



## Constructive Criticism & Solid Alternatives (Mandatory)
Whenever evaluating or planning a solution, you MUST apply constructive criticism. If the initially proposed main solution (whether suggested by the user or generated by the AI) is not strong enough, is inefficient, or contains structural weaknesses, you are forbidden from merely pointing out the flaws. Your constructive criticism MUST immediately be followed by providing a solid, robust, and fully fleshed-out alternative solution. The alternative solution must be demonstrably better, addressing all the weaknesses of the original approach, and you must explain exactly why it is the superior choice.

## 5 Advanced Planning Requirements (Hyper-Intelligent Agent Mode)

**1. Tech Stack & Constraints Lock-in**
The written plan MUST contain a dedicated section clearly defining the permitted and forbidden tools/libraries for this specific task.
* **Example:** *"Rule: Use Next.js for data fetching. Do NOT use `useEffect` for data fetching in this feature."*

**2. Rollback & Contingency Strategy**
An intelligent agent plans for the worst. What if the AI starts writing code, breaks files, and then halts or fails?
* **Solution:** The plan MUST include an instruction to create a safe restore point (e.g., a Git Commit) before beginning any destructive or high-risk step, so we can easily revert if a failure occurs.

**3. Database & Schema Migrations**
If your plan requires modifying a database (e.g., adding a "phone number" column), standard file templates are not enough.
* **Solution:** The AI MUST provide a clear strategy explaining: *"How will we modify the database schema without deleting, corrupting, or losing existing user data?"*

**4. Definition of Done (DoD)**
How do we know the task is truly finished successfully? It is not enough that "the code works."
* **Solution:** The plan MUST include a final checklist of conditions, such as: *"Is the design mobile-responsive? Has the Readme file been updated? Are there any performance regressions?"*

**5. Session Management for Massive Tasks**
AI agents have a limited memory capacity (Context Window). If a plan is massive, the AI will forget instructions halfway through and hallucinate bad code.
* **Solution:** The AI MUST be forced to break large projects down into small, isolated "Milestones." Each milestone must be executed independently in separate sessions to preserve the AI's focus and memory limits.

## Plan File Storage & Location (Mandatory)
The final plan MUST be written and saved as a physical Markdown (`.md`) file. This file MUST be placed inside a dedicated `plans/` directory located at the root of the project. If the `plans/` directory does not currently exist in the project root, you MUST explicitly create it before saving the plan file.
