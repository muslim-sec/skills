# Choosing and running the install

The single most common way this whole process fails is picking a technically-valid install method that doesn't match the person. Optimize for "it works and they can undo it," not for elegance.

## Decision matrix

| Project type | Best method | Why |
|---|---|---|
| Desktop GUI app with official releases | Official installer, `winget`, `brew --cask`, or `.AppImage` | Zero terminal knowledge needed; auto-updates via the package manager |
| Server / web app, especially multi-service (n8n, Supabase, Immich, Open WebUI) | **Docker** | Isolated, dependencies bundled, one command to remove, survives OS updates |
| Python AI/ML project (OpenManus, Cognee) | `uv` virtual environment, or the project's documented path | Never touch system Python; `uv` is far faster and avoids most dependency conflicts |
| Node CLI tool | `npx <pkg>` to try, `npm i -g` once they've committed | `npx` leaves nothing behind if they don't like it |
| Rust / Go project | Prebuilt binary from Releases, or `cargo install` / `go install` | Single static binary — usually the easiest install of all |
| Editor / agent plugin (Understand Anything) | The host's own plugin command | Handles paths and updates for you |
| Browser extension | Store listing if published; otherwise unpacked-load only if they're comfortable | |

**When in doubt between Docker and native: choose Docker for anything that runs as a service, and native for anything with a window.**

## Prerequisites — check before you start

Nothing wastes more goodwill than failing on step 4 of 6. Verify up front:

```bash
docker --version && docker info      # Docker installed AND daemon running
python3 --version                    # exact version — some projects pin 3.12
node --version                       # Node 20+ / 22+ for many modern tools
git --version
uv --version
```

Windows equivalents: `docker --version`, `python --version`, `node --version`, `winget --version`.

If something's missing, install *that* first and say why it's needed. If Docker Desktop isn't installed and they only need one small tool, reconsider — asking someone to install a 600MB runtime for a 5MB utility is bad advice.

## Per-OS package managers

**Windows**
```powershell
winget install -e --id <Publisher.App>      # built into Windows 11 / modern 10
scoop install <app>                          # portable, no admin needed, great for CLI tools
choco install <app>                          # broad catalog, needs admin
```
Prefer `winget` for GUI apps, `scoop` for CLI tools and for users without admin rights.

**macOS**
```bash
brew install <formula>          # CLI tools
brew install --cask <app>       # GUI apps
```
Install Homebrew first if missing: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`. On Apple Silicon, remind them to add `/opt/homebrew/bin` to PATH if the installer's final message says so.

**Linux**
`apt` / `dnf` / `pacman` for anything packaged; otherwise `.AppImage` (chmod +x and run — no install at all), Flatpak, or the project's own script.

## Docker patterns

```bash
# Trial run — nothing persists, clean exit
docker run -it --rm -p 8080:8080 <image>

# Real install — named volume so data survives restarts
docker volume create appdata
docker run -d --name myapp --restart unless-stopped \
  -p 8080:8080 -v appdata:/data <image>

# Multi-service
docker compose up -d
```

Always explain the port mapping in plain terms ("open http://localhost:8080 in your browser") and tell them how to stop and remove it: `docker stop myapp && docker rm myapp`. Knowing the undo makes people willing to try.

If the port is already taken, change the *left* number: `-p 8090:8080`.

## Python project patterns

```bash
# uv — preferred: fast, handles the Python version itself
curl -LsSf https://astral.sh/uv/install.sh | sh     # macOS/Linux
uv venv --python 3.12
source .venv/bin/activate          # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

Windows uv install: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`.

Never `pip install` a project's requirements into the system Python. On Debian/Ubuntu it will refuse (externally-managed-environment) and the flag that forces it is exactly the wrong thing to teach someone.

## Configuration — the step people quit at

Most AI projects need a config file and an API key. The pattern is nearly always:

```bash
cp config/config.example.toml config/config.toml   # or .env.example → .env
```

Then:
- Tell them **which file** and **which line** to edit, and open it for them if you can.
- **Never ask them to paste a real API key into the chat.** They put it in the file directly; you just show the shape: `OPENAI_API_KEY=sk-...`.
- If the tool supports a local model via Ollama, mention it — it removes the API cost question entirely for privacy-minded users.
- Ports, storage paths, and language settings are worth setting now rather than after they hit the default.

## Verify, then teach

Confirm it actually works before declaring victory: open the URL, run `<tool> --version`, check `docker ps`, or just look at the app window. Say explicitly what a good result looks like so they can confirm it themselves.

Then give them **one concrete first action** — not a feature list. "Copy three things, then press Ctrl+Shift+V." "Type this prompt and watch it open a browser." "Import this template workflow." The first success is what makes the tool stick.

Finish with two one-liners they'll need later: how to update, and how to uninstall.

## When you can't reach their machine

Give numbered steps, exact commands in copy-paste blocks, and for each step what success looks like. Ask them to paste back any error output. Offer to walk through it step by step rather than dumping all six steps at once — people follow along better in small increments, and you catch the failure at the step it happened.
