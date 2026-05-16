# Opencode Workflow

Opencode prompts should be commit-sized and scoped to one block. They should not ask for broad rewrites.

## Prompt Anatomy

- Task.
- Context.
- Scope.
- Allowed files.
- Forbidden files.
- Requirements.
- Validation.
- Output format.
- Stop condition.

Require the agent to report touched files and a validation summary. If validation cannot run, require the reason and residual risk.

Good prompts make it clear what not to touch. They separate implementation from audit and release actions.
