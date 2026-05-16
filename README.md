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

Plan -> Block -> Prompt -> Implement -> Validate -> Audit -> Fix -> Commit -> Handoff -> Next block

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
python scripts/validate_playbook_structure.py
python scripts/check_repo_contamination.py
```
