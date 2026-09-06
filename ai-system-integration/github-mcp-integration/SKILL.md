---
name: GitHub MCP Integration
description: Instructions and guidelines for using the Official GitHub MCP Server to search, read, and manage GitHub repositories.
---

# GitHub MCP Integration Skill

This skill activates when you need to interact with GitHub directly. It relies on the `@modelcontextprotocol/server-github` MCP server.

## Capabilities
1. **Repository Search**: Find the best repositories for a given technology.
2. **Code Reading**: Read files directly from public repositories without cloning them.
3. **Issue & PR Management**: Create and review issues or Pull Requests.

## Best Practices
- Always verify the repository URL or owner/name format before querying.
- Do not download large binaries; stick to reading source code files.
- When searching for "the best repository", sort by stars and recent activity.
