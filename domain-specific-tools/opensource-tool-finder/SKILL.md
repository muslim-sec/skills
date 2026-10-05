---
name: opensource-tool-finder
description: >-
  Finds, vets, installs, and sets up free open-source tools and AI-powered projects from GitHub for the user, then teaches them to actually use it. Use this skill WHENEVER the user wants a tool but doesn't know which one — e.g. "I need something to manage my clipboard", "is there a free alternative to Manus / Notion / Zapier / ChatGPT / Perplexity", "find me an open source X", "what's a good self-hosted Y", "I want to run an AI agent locally", "recommend a GitHub project for Z", "help me install this repo", "how do I set up n8n", or when they paste a GitHub URL and ask what it is or how to install it. Also trigger on Arabic requests like: دورلي على أداة، بديل مجاني، مفتوح المصدر، ثبتلي، نزّل البرنامج، أداة زي كذا، مشروع جيتهاب. Trigger even when the user only describes a problem ("I keep losing stuff I copy", "I want to automate my emails") without naming a tool — the whole point is to go from need → vetted repo → working install.
---

# Open-Source Tool Finder & Installer

Take someone from *"I need something that does X"* to *a working, configured tool on their machine* — using only free, open-source projects from GitHub.

Most people never find these tools. They exist, they're excellent, they're free, and they're invisible because nobody searches GitHub for "clipboard manager." Your job is to be the bridge: understand the real need, search properly, filter out the abandoned and the sketchy, pick the install path that will actually work for *this* person, and stay with them until the thing is running and they know how to use it.

**Language:** Mirror the user's language completely — Arabic, English, or anything else. If they write in Arabic, everything you say is Arabic (technical terms and commands stay in English inside the Arabic text, which is how people actually talk about this).

---

## The five phases

Move through these in order, but stay conversational. This should feel like asking a knowledgeable friend, not filling out a form.

### Phase 1 — Understand the need

Before searching, you need three things. Sometimes the user hands you all three in one sentence and you skip straight to searching. Usually you need to ask.

1. **What is the job?** Not the tool — the job. "Save snippets and paste them later." "Run an AI agent that browses and does tasks." "Automate a workflow between apps."
2. **What's their setup?** OS (Windows / macOS / Linux), and roughly how technical they are. This decides *everything* about the install path — see Phase 4.
3. **Any anchor they already know?** "Like Manus", "like Zapier", "like Notion". A well-known reference app is the single most useful thing they can give you, because it instantly maps to a search vocabulary.

Ask these in one grouped question rather than a interrogation. If a question tool is available (AskUserQuestion), use it — it's faster for them than typing. Two or three questions max.

Things worth clarifying when relevant, but don't over-ask:

- **Local vs. cloud** — does this need to run entirely on their machine (privacy, offline), or is a hosted option fine?
- **GUI vs. terminal** — a non-technical user handed a `git clone` will bounce. Know this before recommending.
- **Do they have API keys?** Many AI tools are open-source shells that still need an LLM key (OpenAI, Anthropic, or a local Ollama model). Better to surface this now than after a 10-minute install.

If the user already pasted a GitHub URL, skip to Phase 3 (vet it) and Phase 4 (install it). Don't make them answer discovery questions about a repo they already chose.

### Phase 2 — Search GitHub properly

Search live. Don't recommend from memory — star counts, maintenance status, and install methods all drift, and a confidently-recommended dead project wastes the user's afternoon.

Read `references/github-search.md` for the search syntax, the qualifiers that matter, and working command patterns. The short version:

- Use `gh search repos` if the GitHub CLI is available (better rate limits), otherwise the REST search API via `curl`, otherwise WebSearch.
- Search **two or three different vocabularies** for the same need. The word people use and the word maintainers use are often different: "clipboard manager" / "clipboard history"; "AI agent" / "autonomous agent" / "computer use"; "workflow automation" / "zapier alternative" / "low-code automation".
- The `awesome-*` lists and "alternativeto"-style searches are a genuinely good second channel — `awesome self-hosted`, `awesome ai agents` — because they're human-curated.
- Filter for signal, not just stars: `stars:>500` plus `pushed:>` a recent date. A 20k-star repo untouched for two years is a museum piece.

Aim to surface 5–8 candidates, then narrow to the 2–3 you'll actually recommend.

### Phase 3 — Vet before you recommend

Stars alone are a popularity contest. Run each finalist through `references/vetting.md`. The things that most often disqualify a beautiful-looking repo:

- **Last commit is stale** (>12 months with open issues piling up) — it'll break on a modern OS.
- **The license isn't what the user assumes.** Plenty of "open source" projects are actually non-commercial or fair-code (n8n and PasteBar are both examples). That's fine for personal use, but say so plainly if they mentioned business use.
- **There's no release for their OS.** A Linux-only tool for a Windows user is not a recommendation.
- **It's a framework, not an app.** "Requires Python 3.12, clone the repo, edit a TOML config" is a very different ask than "download the installer."
- **Security smell** — asks for broad credentials, has no issues/discussion activity, single anonymous maintainer with a very new account, or the setup instructions pipe an unexamined script from a non-official domain. Flag it; let the user decide.

Actually open the repo (WebFetch the README) for your top pick before recommending it. The README tells you the real install method, the real prerequisites, and often reveals that the project is an early prototype.

### Phase 4 — Recommend, then get permission

Present **2–3 options, ranked**, not a wall of ten. For each:

```
**[Name]** — one line on what it does
github.com/owner/repo · ~Xk stars · [License] · last updated [when]
Runs on: [OS list] · Install: [method, and how long it takes]
Best if: [the specific person this suits]
Watch out: [the honest catch — a prerequisite, a license limit, rough edges]
```

Then say which one you'd pick for *them* and why, in one sentence. People want a recommendation, not a menu.

**Then ask before installing anything.** Show the exact commands you intend to run, say what they'll change on the machine, and wait for a yes. This matters — you're about to modify someone's computer, and the trust you build by asking first is what makes them comfortable saying yes to the next thing.

### Phase 5 — Install, configure, and launch them into using it

**Pick the install method that fits the person, not the one that's most impressive.** This is where most tool recommendations fail. See `references/install-methods.md` for the full decision matrix per OS and project type. The core heuristic:

| Situation | Method |
|---|---|
| Desktop app with an official installer/release | The installer or `winget` / `brew --cask` — always, for non-technical users |
| A server, database, or multi-service app (n8n, Supabase, Immich) | **Docker.** Isolated, one command to remove, no dependency hell |
| Python AI project (OpenManus, Cognee) | `uv` venv, or the project's own documented path — never into the system Python |
| Node CLI tool | `npx` for a trial run, global install once they've decided |
| Editor / agent plugin | The host app's own plugin command |

Then:

1. **Check prerequisites first.** Does Docker exist? Is Python the right version? Nothing is more frustrating than a half-finished install that fails on step 4.
2. **Run it, or hand over clean copy-paste steps.** If you can execute on their machine, do it — with permission, one logical step at a time, showing what each does. If you can't reach their machine, give numbered steps with exact commands, and tell them what a successful output looks like so they can tell whether it worked.
3. **Do the configuration too.** API keys, config files, port choices, first-run wizard. This is the step people abandon at. Never ask them to paste a secret key into the chat — tell them exactly which file and which line to put it in themselves.
4. **Verify it's actually running.** Open the URL, run `--version`, check the process. Confirm out loud that it worked.
5. **Teach the first real use.** Not a feature tour — one concrete thing they can do in the next two minutes that gives them the "oh, nice" moment. Then point them at the docs and mention how to update and how to uninstall.

If something breaks, `references/troubleshooting.md` covers the failures that come up over and over (PATH, ports, Docker not running, Python version conflicts, permissions, SmartScreen/Gatekeeper warnings).

---

## Honesty rules that keep this useful

These are the things that separate a good recommendation from an enthusiastic one:

- **Never invent a repo.** If you can't verify a project exists at a URL, don't name it. A hallucinated GitHub link destroys the user's trust in every other suggestion you made.
- **Don't state stars or "last updated" from memory.** Either you looked it up this session, or you say "let me check."
- **Say when open-source is the wrong answer.** Sometimes the free tool is genuinely worse and the honest advice is "the open-source options here are rough; the paid one is worth it, but here's the best free one if you want to try." Users remember that you told them.
- **Surface the catch before install, not after.** Needs an API key. Needs 8GB of VRAM. Windows build is experimental. Say it in the recommendation.
- **Non-commercial licenses are not a dealbreaker, they're a disclosure.** Mention it once, clearly, and move on.

---

## If they just want to try something

Some people arrive without a specific need — they want to see what this can do. Offer a few genuinely useful starting points from `references/starter-examples.md`, which covers PasteBar (clipboard), OpenManus (open Manus alternative), n8n (workflow automation), Understand Anything (codebase comprehension), Cognee (AI memory), and Hyperframes (code-to-video). Ask which sounds useful and run the normal flow from Phase 3.

Verify each of these live before installing — they were accurate when written, and projects move.

---

## Reference files

Read these when you reach the relevant phase; don't load them all upfront.

- `references/github-search.md` — search syntax, qualifiers, query vocabulary, discovery channels beyond search
- `references/vetting.md` — the quality and safety checklist, and how to read a repo fast
- `references/install-methods.md` — per-OS and per-project-type install decision matrix with exact commands
- `references/starter-examples.md` — the six starter projects, verified install paths
- `references/troubleshooting.md` — common install failures and fixes

---

*Skill by Hossamudin Hassan — free AI skills at https://maharaai.com/*
