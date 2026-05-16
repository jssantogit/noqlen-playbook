# Context System

Use the smallest context that is safe for the task.

## Tiny Context

- Current task.
- Target files.
- Constraints.
- Validation commands.

Use tiny context for local edits, documentation updates, and small fixes with clear boundaries.

## Standard Context

- Tiny context.
- Active spec.
- Relevant ADR.
- Module context.

Use standard context for non-trivial behavior, app/core boundary work, or changes with multiple touched files.

## Full Context

- Standard context.
- Architecture.
- Handoff.
- Previous audits.
- Broader design history.

Use full context for architecture changes, release preparation, risky file operations, security-sensitive behavior, or cross-repository decisions.
