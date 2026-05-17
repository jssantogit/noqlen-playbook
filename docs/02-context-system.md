# Context System

Use the smallest context that is safe for the task.

Optional tooling may help preserve small context. Context Mode may support context control during a pilot. Serena may support semantic retrieval to avoid reading entire files. RTK may reduce command output noise during exploration.

Tooling does not change the definitions of tiny, standard, or full context.

Raw evidence is still required when context reduction, output routing, or compression would otherwise hide failures, risks, assumptions, touched files, security findings, or stop conditions.

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
