# AGENTS

- Read the relevant context before editing.
- Work only on the requested block.
- Do not perform broad rewrites.
- Do not touch unrelated files.
- Respect allowed and forbidden file lists.
- Do not expose secrets, personal paths, or private data.
- Do not use real music libraries in tests.
- Prefer fake fixtures and dry-run flows.
- Validate before claiming done.
- Report touched files and commands run.
- Always declare Tool Mode when tooling affects the block.
- Do not install or configure agent tooling unless explicitly requested.
- When asked to bootstrap an optimized environment, read the environment docs first.
- Prefer user/global tool configuration over project-local config.
- Do not commit local agent configs.
- Do not create or commit `opencode.json` unless explicitly approved.
- Do not commit `.opencode/`, `.serena/`, `.mcp/`, `.claude/`, `.cursor/`, `.windsurf/`, or `RTK.md`.
- Do not start implementation in the same block as environment setup unless explicitly requested.
- Report installed tools, skipped tools, commands run, configs touched, and verification results.
- Never claim a tool is installed without running a verification command or clearly marking it as unverified.
- If a tool requires manual login, shell restart, PATH change, or user confirmation, report it and stop.
- If using compressed or sandboxed output, preserve raw evidence when relevant.
- Semantic editing tools must obey allowed and forbidden files.
- Caveman/terse-output is forbidden for specs, ADRs, audits, handoffs, releases, and public docs.
- Environment bootstrap and product implementation should be separate blocks unless explicitly requested.
- Stop after the requested block.

## Git Rules

- Do not use `git add .`.
- Stage files explicitly.
- Do not force push.
- Do not rewrite history unless explicitly requested.
