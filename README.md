# Noqlen Playbook

Noqlen Playbook documents the AI-assisted development workflow used across the Noqlen ecosystem. It is a practical operating manual for planning, scoped implementation, validation, audits, handoffs, repository hygiene, and future AI workflows.

This repository is not the beginning of Noqlen. The ecosystem is already mostly built; this playbook preserves the working method so it can be reused for apps, future repositories, future agents, and safer AI-assisted delivery.

## Who Uses It

- Humans planning Noqlen work.
- ChatGPT sessions.
- Opencode/Codex agents.
- Future app teams.
- Future repository maintainers.

## Default Loop

Plan -> Block -> Prompt -> Tool Mode -> Implement -> Validate -> Audit -> Fix -> Commit -> Handoff -> Next block

## Core Principles

- Use the smallest useful context.
- Work in scoped blocks.
- Validate before claiming done.
- Audit meaningful changes.
- Prefer specs before non-trivial changes.
- Use ADRs only for architectural decisions.
- Use fake-first development for integrations.
- Use dry-run before apply.
- Never perform destructive operations without explicit confirmation.
- Never expose secrets, personal paths, lyrics, fingerprints, or private data.
- Never use a real music library in automated tests.
- Keep apps thin over solid cores.

## Context Levels

- `tiny`: current task, target files, constraints, validation commands.
- `standard`: tiny context plus active spec, relevant ADR, and module context.
- `full`: standard context plus architecture, handoff, previous audits, and broader design history.

Use the smallest context that is safe for the task.

## Workflow Accelerators

The Noqlen workflow remains stable:

Plan -> Block -> Prompt -> Tool Mode -> Implement -> Validate -> Audit -> Fix -> Commit -> Handoff -> Next block

Workflow accelerators are optional and explicit. They improve navigation, context control, shell output handling, and CI guardrails, but they are not the workflow itself.

Recommended baseline:

1. OpenCode native capabilities.
2. Serena read-only.
3. RTK / Rust Token Killer for shell-heavy blocks.
4. Context Mode as a pilot for long sessions.
5. Caveman disabled by default.

Tooling cannot bypass scoped blocks, specs, validation, audits, handoffs, repo hygiene, or human review.

## Optimized Development Environment

An optimized development environment may be prepared before coding when a handoff asks for it. Environment bootstrap is a separate block from product implementation unless explicitly requested otherwise.

Prefer global or user-level tool setup. Project-local tooling config is exception-only and must not be committed unless explicitly approved and sanitized.

## Tool Mode

Every tool-assisted block declares Tool Mode. Use `none` when no optional accelerator affects the block. Use specific modes such as `native`, `serena-ro`, `rtk`, `context-mode`, or `combo` when tooling changes how the block is executed.

Tool Mode documents operational support only. It does not reduce the required spec, validation, audit, handoff, or repository hygiene evidence.

## Safety and Evidence

Compressed, routed, or summarized output may help exploration, but it is not audit proof. Raw evidence is required for serious debugging, validation failures, audits, release readiness, boundary changes, and security-sensitive changes.

Do not commit active local agent/tool configs, credentials, auth files, generated tool state, or personal paths. Version only sanitized `.example.*` files.

## App Development Rule

Apps are control and experience layers over solid cores. Heavy domain logic belongs in cores, services, adapters, or explicit contracts, not in UI screens.

## Learning From Local Repositories

The playbook may study local Noqlen repositories read-only to extract reusable workflow lessons. This kind of study must produce sanitized observations only and must never copy private data, secrets, personal paths, lyrics, fingerprints, real library paths, or full local configuration files.

## Repository Map

- `docs/`: workflow documentation.
- `templates/context/`: current context, handoff, delta, and audit summaries.
- `templates/specs/`: requirements, design, tasks, and review templates.
- `templates/adr/`: ADR template.
- `templates/prompts/`: ChatGPT and Opencode/Codex prompt templates.
- `templates/github/`: PR and issue templates.
- `examples/`: safe examples for Aria Core, app shells, and future agents.
- `scripts/`: local validation and contamination checks.

## Validation

```bash
python3 scripts/validate_playbook_structure.py
python3 scripts/check_repo_contamination.py
```
