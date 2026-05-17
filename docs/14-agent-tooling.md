# Agent Tooling

This is the policy overview for optional workflow accelerators. `docs/16-optimized-development-environment.md` covers setup. `docs/17-new-project-environment-bootstrap.md` covers new-project bootstrap.

The Noqlen workflow is already correct and remains unchanged:

Plan -> Block -> Prompt -> Tool Mode -> Implement -> Validate -> Audit -> Fix -> Commit -> Handoff -> Next block

## Purpose

Use tooling to reduce context waste, improve semantic navigation, compress noisy shell output, route long-session context, add CI/security guardrails, or keep temporary status concise. Tooling must preserve scope, evidence, and reviewability.

## Three-Layer Model

1. Workflow: the stable Noqlen loop, specs, validation, audits, handoffs, and repo hygiene.
2. Agent tooling: optional accelerators declared through Tool Mode.
3. Project environment: local or CI setup that supports the project without becoming the workflow.

Tooling is optional. Tooling does not replace the workflow.

## Tool Categories

- Native agent capabilities: built-in OpenCode permissions, planning, execution, review, and sharing controls.
- Semantic navigation/editing: Serena read-only first, edit only inside allowed files.
- Shell output compression: RTK for shell-heavy exploration and noisy output.
- Context/output routing: Context Mode for long sessions, large outputs, and context control during pilots.
- Terse conversation/status: Caveman only for temporary concise status.
- CI/security guardrails: GitHub Actions validation, dependency review, secret scanning, pre-commit, and detect-secrets as optional complementary checks.

## Tool Priority

1. OpenCode native.
2. Serena.
3. RTK.
4. Context Mode.
5. Caveman.

## Tool Mode Values

- `none`: no optional tooling affects the block.
- `native`: OpenCode native capabilities only.
- `serena-ro`: Serena read-only semantic navigation.
- `serena-edit`: Serena semantic editing inside explicit allowed files.
- `rtk`: RTK command output compression.
- `context-mode`: Context Mode routing or long-session support.
- `caveman-limited`: temporary concise status only.
- `combo`: more than one accelerator; list each tool and evidence rule.

## Approved Use Cases

- Locate relevant functions, symbols, tests, and boundaries without reading whole files.
- Summarize noisy test, git, search, or log output during exploration.
- Route large output or long-session context while preserving raw evidence where needed.
- Keep temporary status concise during a long block.
- Add CI checks for structure, contamination, dependency review, and secret scanning.
- Inspect app/core boundaries before editing.

## Forbidden Use Cases

- Replacing specs, validation, audits, handoffs, or human review.
- Editing outside allowed files or bypassing forbidden files.
- Performing broad refactors without explicit block scope.
- Hiding failures, assumptions, risks, touched files, stop conditions, security findings, or boundary changes.
- Treating compressed output, Context Mode output, or tool metrics as audit proof.
- Committing active local agent configs, generated tool state, credentials, auth files, or personal paths.
- Using Caveman or terse-output for specs, ADRs, audits, handoffs, release notes, public docs, or architectural decisions.

## Raw Evidence Policy

Raw evidence is mandatory for serious debugging, validation failures, audits, release readiness, boundary changes, and security-sensitive changes. Summaries may point to raw evidence, but they do not replace it.

Do not compress away touched files, validation commands, raw failures, risks, assumptions, stop conditions, or security findings. If compression hides required detail, rerun the command or capture raw output outside the committed tree.

## Pilot Policy

Pilot one mode at a time on low-risk work. Declare Tool Mode, permissions, allowed files, forbidden files, and raw evidence requirements. Promote a tool only after it improves measurable workflow outcomes without weakening evidence or audit quality.

Context Mode remains pilot/partial for OpenCode until validated in the current environment. RTK telemetry/privacy state must be verified during pilot; Noqlen policy is explicit opt-in only.

## Repo Hygiene Policy

- Prefer global or user-level setup.
- Project-local config is exception-only.
- Do not create or commit `opencode.json` unless explicitly approved.
- Do not commit `.opencode/`, `.serena/`, `.mcp/`, `.claude/`, `.cursor/`, `.windsurf/`, `.mcp.json`, `RTK.md`, active Context Mode state, credentials, or generated agent state.
- Version only sanitized `.example.*` files.
- MCP should prefer local stdio transport. Remote HTTP/SSE MCP servers require explicit exception and security review.
