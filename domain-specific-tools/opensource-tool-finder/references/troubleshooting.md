# Troubleshooting installs

Most failures are one of about ten things. Diagnose from the error text rather than guessing, and tell the user what went wrong in plain language — "the port is already being used by something else" lands better than pasting the stack trace back at them.

## "Command not found" after a successful install

The binary installed but isn't on PATH, or the shell hasn't reloaded.

- Restart the terminal first — this fixes it more often than anything else.
- macOS/Linux: check `echo $PATH`; Homebrew on Apple Silicon needs `/opt/homebrew/bin`. Add the export line to `~/.zshrc` (or `~/.bashrc`) and `source` it.
- Windows: `winget`/`scoop` update PATH but existing terminals keep the old copy — open a new PowerShell window. Check with `$env:PATH -split ';'`.
- npm globals: `npm config get prefix`, then ensure `<prefix>/bin` is on PATH.

## Port already in use

`Error: listen EADDRINUSE` or `port is already allocated`.

Something else owns that port. Change the host side of the mapping — `-p 5679:5678` — or find and stop the other process:
- macOS/Linux: `lsof -i :5678`
- Windows: `netstat -ano | findstr :5678` then `taskkill /PID <pid> /F`

## Docker: "cannot connect to the Docker daemon"

Docker is installed but not running. Start Docker Desktop (Windows/macOS) and wait for the whale icon to settle, or `sudo systemctl start docker` on Linux. On Linux, `permission denied` on the socket means the user isn't in the `docker` group: `sudo usermod -aG docker $USER`, then log out and back in.

## Python version conflicts

Symptoms: `requires Python >=3.12`, or a wheel failing to build.

- Don't fight the system Python. Let `uv` provide the right version: `uv venv --python 3.12`.
- `externally-managed-environment` on Debian/Ubuntu means pip is protecting the system install — the fix is a virtualenv, not `--break-system-packages`.
- If the venv seems ignored, confirm it's active: the prompt should show `(.venv)`, and `which python` should point inside the project.

## Node version too old

`npx` and installs failing with syntax errors usually means Node is old. Install a current LTS via `nvm` (`nvm install 22 && nvm use 22`), `fnm`, or the OS package manager. Check with `node --version`.

## Permission denied

- Linux/macOS: prefer user-level installs over `sudo`. `sudo npm i -g` in particular creates root-owned files that break later updates.
- Windows: some installers need an admin PowerShell. `scoop` deliberately doesn't — use it when the user has no admin rights.
- Downloaded binary won't run on macOS/Linux: `chmod +x <file>`.

## macOS "app is damaged" / unidentified developer

Gatekeeper blocking an unsigned build — normal for small open-source projects. Right-click the app → Open, then confirm. Or System Settings → Privacy & Security → "Open Anyway". Only walk them through this for a repo you've actually vetted.

## Windows SmartScreen warning

"Windows protected your PC" on an unsigned installer — same situation. More Info → Run anyway. Again: only for a repo you've verified.

## Git clone fails

- `Permission denied (publickey)` — they're using an SSH URL without keys set up. Use the HTTPS URL instead.
- Slow or huge clone: `git clone --depth 1 <url>` grabs just the latest snapshot.

## The app starts but does nothing / errors on first action

Almost always configuration:
- Missing or wrong API key — check the `.env` or config file actually got saved, and that the key has no stray quotes or trailing spaces.
- Missing model access — the key is valid but the account lacks access to the model named in the config.
- Wrong config filename — `.env.example` renamed to `.env`, not left as-is.
- Check the logs: `docker logs <name>`, or the terminal output where it's running.

## Install got halfway and failed

Clean up before retrying, or you'll debug a corrupted state:
- Docker: `docker rm -f <name>` and re-run.
- Python: delete `.venv` and rebuild.
- Node: delete `node_modules` and `package-lock.json`, reinstall.
- Cloned repo: delete the folder and clone fresh.

## When to stop and switch approaches

If two attempts at the same install path have failed for different reasons, stop and change strategy rather than grinding — try Docker instead of native, a prebuilt binary instead of a build from source, or the second-ranked project from the recommendation. Tell the user that's what you're doing and why. An hour lost to a stubborn install is worse than a slightly different tool that works in five minutes.
