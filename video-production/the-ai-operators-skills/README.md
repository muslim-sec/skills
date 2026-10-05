# Short-Form Editor Skills — for Claude Code

Two Claude Code skills that turn a raw 9:16 talking-head clip into a finished short:

1. **`cutaway/`** — the rough cut. WhisperX forced alignment gives the exact start/end of every word,
   so the AI can cut on real word edges, remove only the silences (the no-word gaps), and arrange the
   best takes into one flowing story (hook → … → CTA). Output is a cut list + a matching MP4.
2. **`finish/`** — the styling pass. Reframe to 9:16, animated zooms / punch-ins, lens effects, an
   exponential text fade-in, the "authority stack" text look, captions, and SFX timed to motion.

They run in order: **cutaway locks the cut → finish styles it.**

## Install

Drop each folder into your Claude Code skills directory:

```bash
cp -R cutaway ~/.claude/skills/shortform-cutaway
cp -R finish  ~/.claude/skills/shortform-finish
```

Then in Claude Code just hand it a clip and say what you want — e.g. *"make the rough cut, remove the
silences"* (cutaway) or, once the cut is locked, *"finish this short, add the hook zoom"* (finish). The
skill descriptions trigger automatically.

**One-time setup for cutaway:** it needs WhisperX in a Python 3.11 venv. The skill's `## SETUP` section
walks you through it (`python3.11 -m venv ~/wx-env && ~/wx-env/bin/pip install whisperx`). That's the only
dependency; the cut scripts take all paths as arguments, so there's nothing to hardcode.

## First run — which editor do you use?

On the first run, each skill asks **which editor you edit in** and follows the matching branch:

- **DaVinci Resolve** — the cut lands as a timeline; zooms are built as Fusion comps.
- **Premiere Pro** — the cut lands as an EDL/XML; zooms/text via keyframes + Essential Graphics.
- **Remotion** — everything is code; the cut is a playlist of segments, effects are `interpolate` curves.
- **Claude-Code-only (no NLE)** — the cut renders straight to an MP4 with ffmpeg; no other software needed.

Don't have an editor? Pick **Claude-Code-only** — it produces a finished, postable MP4 on its own.

## A note on the visual style

These skills teach the **method**, not a pile of finished assets. The cutaway is fully turnkey — it
produces the cut. The finish skill gives you the *techniques* (the zoom curves, the exponential fade, the
authority-stack text look, the sound-matches-motion rules) so you recreate the look with **your own
footage, your own SFX, and your own style graphics**. Build that small library once; it's yours to keep.
