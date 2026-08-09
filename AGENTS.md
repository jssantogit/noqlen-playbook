# AGENTS

These are repository invariants for AI-assisted work. Keep them short and durable.

## Work Discipline

- Inspect the relevant code and current repository state before editing.
- Make the smallest complete and coherent change that satisfies the request.
- Do not perform unrelated rewrites or refactors.
- Do not keep a diff artificially small at the cost of correctness or maintainability.
- Respect explicit user scope and repository boundaries.
- Validate changed behavior before claiming completion.
- When cheap and relevant, observe the actual user-visible/runtime outcome instead of relying only on implementation claims.
- Review the final diff for scope drift, accidental changes, and residual risk.
- If validation cannot run, report why and what remains unverified.
- Do the workflow; do not narrate step names, inactive escalations, risk tiers, Tool Mode, or process metadata unless they materially help the user or reviewer.
- Split or delegate work only when feedback cycles, independent parallelism, context isolation, or independent scrutiny justify the coordination cost.
- Keep one coordinator responsible for integrating delegated work and verifying the combined result.
- When the same correction or failure recurs, improve an executable guardrail, reusable skill/procedure, or discoverable documentation instead of repeatedly expanding prompts.

## Safety

- Do not commit or unnecessarily reproduce secrets, credentials, tokens, personal paths, private data, lyrics, fingerprints, or real music-library data.
- User-authorized private/local data may be inspected transiently when the task requires it; minimize what is copied into durable or shareable artifacts.
- Automated tests must use synthetic data or sanitized fixtures, not a real user music library.
- Implement and test dangerous capabilities in isolated state; do not require user confirmation merely to run safe tests.
- An explicit user request for a named action on a sufficiently defined target counts as authorization for that action; do not ask for the same confirmation twice.
- Ask again only if target/scope is materially ambiguous, the action expands beyond authorization, consequences materially increase, or the tool/platform requires confirmation.
- Before a high-impact real-state mutation that has not already been authorized, require explicit apply intent.
- Prefer dry-run, preview, temporary workspaces, backups, or reversible operations only when they reduce a concrete failure mode.
- Do not publish, deploy, merge, release, force push, or rewrite history unless explicitly requested.
- Keep local agent/tool configuration and generated agent state untracked unless an explicitly approved sanitized example is the task.
- Treat third-party skills, plugins, MCP servers, and agent packages as software trust dependencies; inspect them, minimize privileges, and pin/version durable dependencies when reproducibility matters.

## Architecture And Testing

- Follow existing boundaries unless changing them is part of the request.
- Keep heavy domain logic out of UI screens and thin app shells.
- Do not invent an abstraction only to create a fake.
- Isolate real external or nondeterministic dependencies during verification when direct use would be unsafe, impractical, flaky, expensive, or dependent on private state.
- Use isolated workspaces for concurrent writers when interference is possible; read-only parallel investigation does not require a worktree by default.
- Use ADRs only for architectural decisions that are meaningfully hard to reverse.
- Routine edits to an established public API do not require an ADR unless they change durable API strategy or boundary policy.
- Diff size or task duration alone does not require formal audit, delegation, planning, or branch isolation.
