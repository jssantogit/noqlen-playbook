# AI Development Workflow

The main Noqlen loop is:

1. Clarify goal.
2. Define block.
3. Select context level.
4. Generate Opencode prompt.
5. Implement.
6. Validate.
7. Audit.
8. Fix.
9. Commit.
10. Update handoff.
11. Move to next block.

## Tool Roles

ChatGPT handles planning, architecture, breaking work into blocks, writing prompts, reviewing audit reports, and deciding next steps.

Opencode/Codex edits files, implements scoped blocks, runs tests, produces validation summaries, and audits repository state.

GitHub provides source history, issues, PRs, review, CI, releases, and durable documentation.

Each tool has a bounded role. Planning does not imply implementation. Implementation does not imply release. Audits identify risk before the next block starts.

## Retrospective Learning

Past Noqlen repositories can be studied read-only to improve future prompts, examples, guardrails, and handoffs. The output should be sanitized workflow lessons, not copied private context or blame language. The question is: how would the current workflow handle this kind of change better now?
