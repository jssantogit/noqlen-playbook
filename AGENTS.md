# AGENTS

These are repository invariants for AI-assisted work. Keep them short and durable.

## Work Discipline

- Inspect the relevant code and current repository state before editing.
- Make the smallest complete and coherent change that satisfies the request.
- Do not perform unrelated rewrites or refactors.
- Do not keep a diff artificially small at the cost of correctness or maintainability.
- Respect explicit user scope and repository boundaries.
- Validate changed behavior before claiming completion.
- Review the final diff for scope drift, accidental changes, and residual risk.
- If validation cannot run, report why and what remains unverified.
- Do the workflow; do not narrate step names, inactive escalations, risk tiers, Tool Mode, or process metadata unless they materially help the user or reviewer.

## Safety

- Never expose or commit secrets, credentials, tokens, personal paths, private data, lyrics, fingerprints, or real music-library data.
- Automated tests must use synthetic data or sanitized fixtures, not a real user music library.
- Implement and test dangerous capabilities in isolated state; do not require user confirmation merely to run safe tests.
- Before performing destructive, publishing, production, history-rewriting, or other high-impact actions against real state, require explicit apply intent when that action has not already been authorized.
- Prefer dry-run, preview, temporary workspaces, backups, or reversible operations before destructive real-state changes when practical.
- Do not publish, deploy, merge, release, force push, or rewrite history unless explicitly requested.
- Keep local agent/tool configuration and generated agent state untracked unless an explicitly approved sanitized example is the task.

## Architecture And Testing

- Follow existing boundaries unless changing them is part of the request.
- Keep heavy domain logic out of UI screens and thin app shells.
- Do not invent an abstraction only to create a fake.
- Isolate real external or nondeterministic dependencies during verification when direct use would be unsafe, impractical, flaky, expensive, or dependent on private state.
- Use ADRs only for architectural decisions that are meaningfully hard to reverse.
- Routine edits to an established public API do not require an ADR unless they change durable API strategy or boundary policy.
- Diff size alone does not require formal audit.

## Git

- Prefer explicit staging over `git add .` when working interactively.
- Do not force push.
- Do not rewrite history unless explicitly requested.
