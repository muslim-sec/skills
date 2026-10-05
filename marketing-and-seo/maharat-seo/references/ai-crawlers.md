# AI Crawlers — robots.txt Reference

Check `robots.txt` for these user-agents and report which are allowed/blocked.
A site that blocks AI search crawlers cannot be cited by those engines.

| Crawler (user-agent) | Owner | Purpose | Recommendation |
|----------------------|-------|---------|----------------|
| `GPTBot` | OpenAI | ChatGPT training/index | Allow for AI visibility |
| `OAI-SearchBot` | OpenAI | ChatGPT search results | **Allow** (search surface) |
| `ChatGPT-User` | OpenAI | ChatGPT live browsing | Allow |
| `ClaudeBot` | Anthropic | Claude web features | Allow |
| `anthropic-ai` | Anthropic | Claude training | Optional |
| `PerplexityBot` | Perplexity | Perplexity search | **Allow** (search surface) |
| `Perplexity-User` | Perplexity | Perplexity live fetch | Allow |
| `Google-Extended` | Google | Gemini/Vertex training (separate from Googlebot) | Optional; blocking it does NOT remove you from Google Search |
| `Googlebot` | Google | Search + AI Overviews | **Never block** |
| `Bingbot` | Microsoft | Bing + Copilot | **Never block** |
| `CCBot` | Common Crawl | Training data | Block if you don't want training use |
| `Bytespider` | ByteDance | TikTok/Douyin AI | Often blocked |
| `cohere-ai` | Cohere | Cohere models | Optional |

## Distinguish "search" from "training"
Some owners run separate bots for *search citation* vs *model training*. Blocking
training crawlers (`GPTBot`, `Google-Extended`, `CCBot`) does **not** by itself
remove you from the AI **search** surfaces — those use the search bots
(`OAI-SearchBot`, `Googlebot`, `Bingbot`, `PerplexityBot`). Make this distinction
clear in the report so the user can choose: be cited in AI answers, opt out of
training, or both.

## Recommended starter directives (AI search visible, training optional)
```
# Allow AI search surfaces
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /

# Optional: opt out of model training while staying in AI search
User-agent: GPTBot
Disallow: /
User-agent: Google-Extended
Disallow: /
User-agent: CCBot
Disallow: /

Sitemap: https://example.com/sitemap.xml
```
Always tailor to the user's stated preference; present the trade-off, don't decide for them.
