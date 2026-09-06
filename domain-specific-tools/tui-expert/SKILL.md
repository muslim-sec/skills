---
name: tui-expert
description: >-
  Best practices for building Terminal User Interfaces (TUI) and TTY windowed applications.
---

# Terminal User Interface (TUI) Design

When building interactive windowed terminal applications (TUIs), adhere to these standards:

## 1. Framework Selection
Never build a TUI from scratch using raw ANSI escape codes. Always use a proven framework:
- **Python:** Use `Textual` (for full apps) or `Rich` (for beautiful CLI output).
- **Go:** Use `Bubbletea` (Elm architecture) and `Lipgloss` (styling).
- **Rust:** Use `Ratatui`.
- **Node.js:** Use `Ink` (React for CLI) or `blessed`.

## 2. Responsive Layouts
- Terminals can be resized dynamically (SIGWINCH signal).
- Your TUI must handle window resizing gracefully. Use flexbox-like grid systems provided by your framework (e.g., Lipgloss grids, Textual CSS).

## 3. The Event Loop & State
- TUI apps must run non-blocking. Do not use blocking `sleep()` or `input()`.
- Use an asynchronous event loop to listen for keyboard events while rendering the UI.

## 4. Keyboard Navigation
- Provide Vim-style keybindings (`h`, `j`, `k`, `l`) alongside arrow keys for navigation.
- Always map `q` or `Ctrl+C` to quit gracefully.
- Display a bottom status bar showing available keybindings (e.g., `[q] quit  [tab] switch tab  [enter] select`).

## 5. Color Fallbacks
- Not all terminals support TrueColor (24-bit). Use standard 16 or 256 colors as fallbacks.
- Check the `COLORTERM` environment variable.
