---
name: GitHub Repo Mapper
description: Analyzes GitHub repositories to generate architectural Mermaid mind maps, structural AST indexes, and dependency graphs.
---

# GitHub Repo Mapper Skill

Use this skill to deeply understand any unfamiliar GitHub repository by visualizing its structure.

## Capabilities
1. **Mermaid Mind Maps**: Generate comprehensive `mermaid` diagrams mapping out the core directories and their purposes.
2. **Architecture Visualization**: Map out the class, function, and import graphs of a repository to understand how components interact.
3. **Dependency Analysis**: Identify the main frameworks and libraries driving the repository.

## Execution
- Use tree-sitter or the `graphify` tool to build structural indexes of the codebase.
- Always output the mind map in a markdown artifact so the user can easily visualize it.
