# Vetting a repo before you recommend it

The goal is to avoid two specific failures: recommending something that's dead, and recommending something that's unsafe. Both waste far more of the user's time than the extra two minutes of checking costs you.

## The fast pass — six checks

Run these on every finalist. WebFetch the repo page and README; that's usually enough for all six.

**1. Is it alive?**
Last commit within ~6 months is healthy. 6–12 months is fine for a small, finished, stable tool (a clipboard manager doesn't need weekly commits) but suspicious for anything touching AI APIs, browsers, or OS internals — those break from the outside. Over 12 months with a pile of unanswered issues means it will probably fail on install.

**2. Do the stars make sense?**
Not "are there enough" — does the ratio look real? Thousands of stars with a handful of forks, no issues, and three commits is a red flag for an inflated repo. Healthy projects have discussion: issues opened *and* closed, PRs merged, releases tagged.

**3. What's the license, really?**
Read the actual license field, don't assume. Categories worth distinguishing for the user:

- **Permissive (MIT, Apache-2.0, BSD)** — do anything, including commercial.
- **Copyleft (GPL, AGPL)** — free to use; matters only if they're redistributing or building a product on top. AGPL specifically affects SaaS use.
- **Fair-code / source-available (n8n's Sustainable Use License, BSL, Elastic)** — free to self-host for their own use, restricted for reselling. Fine for individuals, needs a mention if they said "for my company."
- **Non-commercial (CC BY-NC — PasteBar uses this)** — personal use free, business use needs permission.

State the category in plain words once. Don't lecture.

**4. Is there a build for their OS?**
Check the Releases page, not just the README's claims. "Cross-platform" in a README sometimes means "compiles on Linux if you're patient." Look for actual `.exe`/`.msi`, `.dmg`, `.AppImage`/`.deb` assets, or a published package.

**5. How hard is it really to install?**
Read the README's install section and classify honestly:
- *Installer / package manager / single binary* → anyone can do this
- *Docker one-liner* → anyone who can install Docker
- *`npx` / `pip install`* → comfortable-with-terminal users
- *Clone + venv + edit config file + supply API key* → this is a project, not a product. Say so.

**6. Does it need anything expensive or unobvious?**
An LLM API key. A GPU with enough VRAM. A separate database. Node 22+. Python 3.12 exactly. A paid account somewhere. Surface every one of these in the recommendation, before install.

## Security smell tests

Open-source doesn't mean safe. Flag — don't silently refuse — when you see:

- **Install instructions piping a script from a non-official domain** into a shell. `curl … | bash` from the project's own GitHub raw URL or its documented site is standard practice; from a random shortener or unrelated host, it isn't.
- **A single, very new, anonymous maintainer account** on a project asking for broad credentials.
- **Requests for credentials it has no reason to need** — a clipboard tool wanting cloud storage tokens, a "free" AI wrapper wanting your full Google account.
- **No issues, no discussions, no forks, but heavy promotion.** Real usage leaves traces.
- **Obfuscated or minified code in the repo itself**, or binaries committed without a build pipeline.
- **A name that shadows a well-known project** in a different org — always confirm you're at the canonical repo. (Typosquatted namespaces are common for popular tools.)

When something smells off, tell the user what you noticed and let them decide. They may have context you don't.

## Choosing between finalists

When two projects are close, prefer the one that is:

- **Easier to install for this specific person.** A slightly worse tool they can actually run beats a better one they abandon at step 3.
- **Better documented.** Docs quality predicts the whole support experience.
- **Backed by more than one person.** Solo projects vanish.
- **Reversible.** Docker and portable apps uninstall cleanly. Something that scatters files across the system doesn't.

Say which one you'd pick and why. A ranked recommendation with a reason is more useful than a neutral comparison table.
