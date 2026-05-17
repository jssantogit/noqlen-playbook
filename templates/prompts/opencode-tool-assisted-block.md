# Opencode Prompt: Tool-Assisted Block

Purpose: Implement one scoped block with an explicit optional Tool Mode.

## Prompt

Task: `<block task>`

Block: `<block name>`

Goal: `<goal>`

Context level: `<tiny | standard | full>`

Tool Mode: `<none | native | serena-ro | serena-edit | rtk | context-mode | caveman-limited | combo>`

Tooling goal: `<navigation | shell compression | long-session routing | concise status | CI/security guardrails | none>`

Scope: `<scope>`

Allowed files: `<allowed files>`

Forbidden files: `<forbidden files>`

Tool permissions: `<what the tool may do>`

Execution policy: tooling is optional and cannot bypass specs, validation, audits, handoffs, repo hygiene, allowed files, forbidden files, or stop conditions.

Raw evidence requirements: `<raw failures, audit evidence, or logs to preserve>`

Compression limits: compressed output is allowed only during exploration. Final audit and failure evidence must remain complete enough to review.

Forbidden tooling artifacts unless explicitly approved and sanitized: `opencode.json`, `.opencode/**`, `.serena/**`, `.mcp/**`, `.mcp.json`, `RTK.md`, `.claude/**`, `.cursor/**`, `.windsurf/**`, generated tool state, provider auth files, credentials, and secrets.

Requirements: `<requirements>`

Validation: `<commands>`

Output format: touched files, tool mode used, tooling goal, commands compressed, validation summary, raw evidence status/location, config files touched, risks, and whether the block is complete.

Stop condition: stop after this block, if forbidden files are needed, if validation changes scope, if raw failure evidence is unavailable, or if destructive actions would be required.
