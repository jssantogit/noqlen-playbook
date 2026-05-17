# AI Development Workflow

The main Noqlen loop is:

1. Clarify goal.
2. Define block.
3. Select context level.
4. Generate Opencode prompt.
5. Declare Tool Mode.
6. Implement.
7. Validate.
8. Audit.
9. Fix.
10. Commit.
11. Update handoff.
12. Move to next block.

Short form:

Plan -> Block -> Prompt -> Tool Mode -> Implement -> Validate -> Audit -> Fix -> Commit -> Handoff -> Next block

## Tool Roles

ChatGPT handles planning, architecture, breaking work into blocks, writing prompts, reviewing audit reports, and deciding next steps.

Opencode/Codex edits files, implements scoped blocks, runs tests, produces validation summaries, and audits repository state.

GitHub provides source history, issues, PRs, review, CI, releases, and durable documentation.

Each tool has a bounded role. Planning does not imply implementation. Implementation does not imply release. Audits identify risk before the next block starts.

Optional agent tooling may support context control, command output compression, semantic navigation, or concise status. Tooling is an efficiency layer only; it does not replace specs, validation, audits, or human review.

Tool Mode is the explicit declaration of that optional layer. Use `none` when no accelerator affects the block. Tooling cannot change the central loop or remove required evidence.

## Retrospective Learning

Past Noqlen repositories can be studied read-only to improve future prompts, examples, guardrails, and handoffs. The output should be sanitized workflow lessons, not copied private context or blame language. The question is: how would the current workflow handle this kind of change better now?
