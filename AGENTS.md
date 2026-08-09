# AGENTS

These are repository invariants for AI-assisted work. Keep them short and durable.

## Work Discipline

- Inspect the relevant code and current repository state before editing.
- Make the smallest coherent change that satisfies the request.
- Do not perform unrelated rewrites or refactors.
- Respect explicit user scope and repository boundaries.
- Validate changed behavior before claiming completion.
- Review the final diff for scope drift, accidental changes, and residual risk.
- If validation cannot run, report why and what remains unverified.

## Safety

- Never expose or commit secrets, credentials, tokens, personal paths, private data, lyrics, fingerprints, or real music-library data.
- Automated tests must use synthetic data or sanitized fixtures, not a real user music library.
- Destructive, publishing, production, migration, authentication, or security-sensitive actions require the Safety Gate in `docs/safety.md`.
- Prefer dry-run, preview, temporary workspaces, backups, or reversible operations before destructive changes when practical.
- Do not publish, deploy, merge, release, force push, or rewrite history unless explicitly requested.
- Keep local agent/tool configuration and generated agent state untracked unless an explicitly approved sanitized example is the task.

## Architecture And Testing

- Follow existing boundaries unless changing them is part of the request.
- Keep heavy domain logic out of UI screens and thin app shells.
- Do not invent an abstraction only to create a fake.
- Use fakes, fixtures, stubs, or emulators when a real external or nondeterministic boundary benefits from isolation.
- Use ADRs only for architectural decisions that are meaningfully hard to reverse.

## Git

- Prefer explicit staging over `git add .` when working interactively.
- Do not force push.
- Do not rewrite history unless explicitly requested.
