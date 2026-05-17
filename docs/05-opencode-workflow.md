# Opencode Workflow

Opencode prompts should be commit-sized and scoped to one block. They should not ask for broad rewrites.

## Prompt Anatomy

- Task.
- Context.
- Environment mode.
- Install scope.
- Scope.
- Allowed files.
- Forbidden files.
- Tool Mode.
- Tool permissions.
- Raw evidence policy.
- Raw evidence requirements.
- Compression limits.
- Config files touched.
- Requirements.
- Validation.
- Output format.
- Stop condition.

Require the agent to report touched files and a validation summary. If validation cannot run, require the reason and residual risk.

Good prompts make it clear what not to touch. They separate implementation from audit and release actions.

Tool Mode should be explicit when optional tooling is used. Compression may reduce noisy exploration output, but final failure evidence and audit evidence must remain reviewable.

Before coding in a new project, Opencode may run the optimized environment bootstrap block. Environment bootstrap is separate from product implementation. Tool Mode should be declared after bootstrap, and the agent must report tooling state before starting implementation.

OpenCode native capabilities are the first accelerator layer. Prefer explicit permissions for risky operations, disabled or manual share for real Noqlen work, and global/user-level config over project-local config. Do not create or commit `opencode.json` or `.opencode/` unless explicitly approved and sanitized.
