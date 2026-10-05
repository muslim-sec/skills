# Searching GitHub for the right project

## Which tool to reach for

Try in this order, falling back when one isn't available:

1. **`gh` CLI** — best rate limit (30 searches/min, uses the user's auth), cleanest output.
2. **REST search API via `curl`** — works with no token at 10 searches/min.
3. **WebSearch** — always works, and is genuinely better for "what do people recommend as an alternative to X" style questions where community opinion matters more than metadata.

Use more than one. The API gives you metadata; the web gives you judgment.

## `gh` CLI

```bash
gh search repos "clipboard manager" --stars=">500" --sort=stars --limit=10

gh search repos --topic=ai-agent --language=python --stars=">1000" \
  --updated=">2026-01-01" --sort=stars --limit=20 \
  --json fullName,stargazersCount,description,updatedAt,license
```

Two gotchas:
- Quote any value containing `>` or `<` (`--stars=">500"`), or the shell reads it as a redirect.
- Qualifiers with no matching flag go after a `--` separator: `gh search repos "x" -- -topic:linux`.

Useful flags: `--topic`, `--language`, `--license`, `--stars`, `--updated`, `--created`, `--archived=false`, `--limit`, `--json`.

## REST API with curl

Endpoint: `GET https://api.github.com/search/repositories`

```bash
curl -s -H "Accept: application/vnd.github+json" \
  "https://api.github.com/search/repositories?q=clipboard+manager+stars:%3E500&sort=stars&order=desc&per_page=10" \
  | jq -r '.items[] | "\(.full_name)\t\(.stargazers_count)★\t\(.license.spdx_id // "no-license")\tpushed \(.pushed_at[:10])\t\(.description)"'
```

URL-encode `>` as `%3E`, `<` as `%3C`; spaces become `+`. Add `-H "X-GitHub-Api-Version: 2022-11-28"` to pin the version.

Unauthenticated search is limited to **10 requests/minute** and **1000 results per query** — so make each query count rather than paginating deep.

If `api.github.com/search/*` is blocked in the environment (some sandboxes only allow repo-scoped paths), fall back to WebSearch with `site:github.com` and then WebFetch the specific repo pages.

## Qualifiers that actually matter

| Qualifier | Why it matters |
|---|---|
| `stars:>500` | Crude popularity floor. Use `>100` for niche needs — good tools in small niches never hit 1k. |
| `pushed:>2026-01-01` | **The most important filter.** Separates living projects from archives. |
| `archived:false` | Excludes explicitly retired repos. |
| `license:mit` / `apache-2.0` | Only when the user cares about commercial use. |
| `topic:` | Higher signal than free text — maintainers tag deliberately. |
| `language:` | Use as a proxy for install method: `python` → venv, `typescript` → npm/npx, `rust`/`go` → single binary (usually the easiest install of all). |
| `in:readme` | Widens a narrow keyword search when name/description matching returns too little. |

## Search vocabulary — the part people get wrong

Users describe needs in end-user language; maintainers describe repos in developer language. Search both.

| The user says | Also search |
|---|---|
| "save things I copy" | clipboard manager, clipboard history, snippet manager |
| "AI agent like Manus" | autonomous agent, general AI agent, computer use agent, agent framework |
| "automate between apps" | workflow automation, zapier alternative, low-code automation, n8n |
| "chat with my documents" | RAG, document QA, knowledge base, local LLM chat |
| "notes app" | personal knowledge management, PKM, second brain, markdown notes |
| "screen recorder" | screen capture, screencast, screen recording |
| "self-hosted Google Photos" | photo management, self-hosted photos, media library |
| "AI memory for my agent" | agent memory, long-term memory, knowledge graph memory |

Also just search `"<well-known app> alternative"` — both on GitHub and on the web. The community writes these comparisons constantly.

## Discovery channels beyond raw search

- **`awesome-*` lists** — `gh search repos "awesome self-hosted"`, `awesome ai agents`, `awesome windows apps`. Human-curated, and the annotations tell you what each project is actually for.
- **`awesome-selfhosted`** specifically is the best single index for anything server-side.
- **Web search for "best open source X 2026"** — surfaces what people actually run day to day, which star counts don't capture.
- **The README of the closest project you already found** — good projects link to their peers and predecessors in a comparison table.
- **GitHub topic pages** — `github.com/topics/<topic>` is browsable and sorted usefully.

## Reading results fast

For each candidate you're considering, you want these six fields before deciding anything: name, stars, license, last push date, primary language, one-line description. Present them compactly — a table or a tight block per repo — so the user can scan rather than read.
