# Starter examples

Six projects worth suggesting when someone wants to see what's possible but hasn't named a need. They span the main categories: a desktop utility, an AI agent, a self-hosted service, a dev tool, an AI infrastructure library, and a creative tool.

**Verify before installing.** These details were accurate when this skill was written; stars, versions, and install commands drift. Fetch the repo and confirm the current install instructions rather than pasting from here blindly. Don't quote star counts you haven't checked this session.

---

## PasteBar — clipboard manager
`github.com/PasteBar/PasteBarApp` · Windows, macOS · License: CC BY-NC (non-commercial; has a limited commercial exception)

Unlimited clipboard history plus saved snippets you can paste anytime — the answer to "I need to keep text around and reuse it."

```powershell
winget install -e --id PasteBar.PasteBar
```
macOS: no Homebrew cask — download the `.dmg` from the Releases page or pastebar.app.

*Note the non-commercial license if they mention work use.*

---

## OpenManus — open-source general AI agent
`github.com/FoundationAgents/OpenManus` · Cross-platform · MIT · needs Python 3.12 + an LLM API key

The most-cited free alternative to Manus: an agent that plans and executes multi-step tasks. It's a framework you run from the terminal, not a polished app — set expectations accordingly.

```bash
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
uv venv --python 3.12 && source .venv/bin/activate
uv pip install -r requirements.txt
playwright install                                    # optional, for browser tasks
cp config/config.example.toml config/config.toml      # add your API key here
python main.py
```

---

## n8n — workflow automation
`github.com/n8n-io/n8n` · Cross-platform · Sustainable Use License (fair-code, not OSI)

Self-hosted Zapier/Make alternative with 400+ integrations and native AI nodes. **Install with Docker** — it's a service with state, and Docker keeps it isolated and removable.

```bash
docker volume create n8n_data
docker run -d --name n8n --restart unless-stopped \
  -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```
Then open http://localhost:5678. `npx n8n` works for a quick look but doesn't persist as cleanly.

---

## Understand Anything — make sense of any codebase
`github.com/Egonex-AI/Understand-Anything` · macOS, Linux, Windows · MIT

Turns a codebase into an explorable knowledge graph you can question. It's a plugin for AI coding agents (Claude Code, Cursor, Copilot, Codex, Gemini CLI), not a standalone app.

Claude Code:
```
/plugin marketplace add Egonex-AI/Understand-Anything
/plugin install understand-anything
```
macOS/Linux: `curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash`
Windows: `iwr -useb https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.ps1 | iex`

---

## Cognee — memory for AI agents
`github.com/topoteretes/cognee` · Cross-platform · Apache-2.0 · Python 3.10+

Gives agents persistent long-term memory through a self-hosted knowledge graph. For developers building on top of LLMs rather than end users.

```bash
pip install cognee          # or: uv pip install cognee
```
Docker: `docker run --env-file ./.env -p 8000:8000 --rm -it cognee/cognee:main`
Also has TypeScript (`@cognee/cognee-ts`) and Rust clients.

---

## Hyperframes — write HTML, render video
`github.com/heygen-com/hyperframes` · Cross-platform · Apache-2.0 · needs Node 22+ and FFmpeg

Deterministic HTML/CSS → MP4 rendering built for AI agents to drive. A Remotion-style approach to programmatic video.

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview     # live browser preview
npx hyperframes render      # export MP4
```
Confirm you're at the `heygen-com` org — other namespaces with this name exist.

---

## Using these well

Don't recite the list. Ask what kind of thing would actually help them — "something for your desktop, an AI agent you can run yourself, or automation between apps?" — then offer the one or two that fit and run the normal vetting and install flow. The list is a conversation starter, not a catalog.
