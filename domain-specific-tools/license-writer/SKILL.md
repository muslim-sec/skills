---
name: License Writer
description: Analyzes project requirements and generates appropriate open-source (MIT, GPL, Apache) or closed-source commercial licenses.
---

# License Writer Skill

Use this skill when the user asks to generate, update, or analyze a software license for their project.

## Open Source Capabilities
- **MIT License**: Generate when the user wants maximum permissiveness and no warranty.
- **GNU GPLv3**: Generate when the user wants to ensure derived works are also open-sourced.
- **Apache 2.0**: Generate when the user needs explicit patent rights and trademark protections.

## Closed Source / Commercial Capabilities
- **Proprietary EULA**: Generate End-User License Agreements restricting distribution, modification, or reverse engineering.
- **SaaS Terms of Service**: Generate customized terms for web-based services.

## Execution Rules
1. Ask the user about their monetization strategy and code-sharing preferences before drafting the license.
2. Always write the final license to a file named `LICENSE` in the root of their repository.
3. Add a clear copyright header with the current year and the user's/company's name.
