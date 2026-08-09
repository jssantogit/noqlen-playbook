# Tooling

Tooling is an optional acceleration layer. It is **not a step in the Noqlen workflow** and normal tasks do not declare a Tool Mode.

The workflow remains:

```text
Inspect -> Implement -> Verify -> Review
```

Use tools when they reduce real work, context waste, elapsed time, or risk without hiding evidence or expanding permissions unnecessarily.

## Capabilities Before Brands

Organize the working environment around capabilities, not today's preferred product names.

Useful capability groups include:

- repository search and code navigation;
- reusable skills/procedures;
- subagents and parallel execution;
- isolated workspaces/worktrees;
- permissions and sandboxing;
- hooks and deterministic policy checks;
- test/build/runtime observability;
- context compaction and retrieval;
- MCP or other external tool connections;
- background/recurring automation.

Specific tools are implementations of these capabilities and may change over time.

## Native Capabilities First

Prefer capabilities already provided by the active agent/runtime before installing another layer.

Native search, planning, subagents, worktrees, permissions, sandboxing, compaction, browser/runtime inspection, and CI integrations often eliminate the need for separate plugins.

Add another tool only when it provides measurable value the native environment does not already provide well.

## Skills And Reusable Procedures

Use a skill/procedure when a workflow is:

- repeated across tasks;
- specific enough to benefit from reusable instructions;
- too detailed for durable repository invariants;
- valuable to load only when relevant.

Good skills are focused and use progressive disclosure: keep the discoverable description small, then load deeper instructions/scripts/references only when the skill is selected.

Do not turn every task type into a skill. A one-off instruction belongs in the task prompt. A durable invariant belongs in `AGENTS.md`. A deterministic rule belongs in executable tooling when practical.

Recommended hierarchy:

```text
executable rule -> reusable skill -> discoverable docs -> prompt instruction
```

Treat third-party skills as executable trust dependencies when they can run scripts or influence tool use. Inspect their source, minimize privileges, and pin/version durable dependencies when reproducibility matters.

## Subagents And Delegation

Use subagents when separate context or independent execution materially improves the task.

High-value uses include:

- parallel read-only investigation of independent questions;
- focused security/API/migration review;
- independent test or failure analysis;
- independent implementation units with stable boundaries;
- long exploration that can be summarized back to the coordinator.

Keep one coordinator responsible for scope, integration, and final verification.

Do not create a fixed `planner -> coder -> tester -> reviewer` pipeline for routine work. Multiple agents are useful when they buy parallelism, context isolation, or independent scrutiny — not because agent count itself is a quality metric.

## Workspaces And Worktrees

Use isolated workspaces/worktrees/branches when concurrent writers could interfere with each other or when isolation materially reduces operational risk.

Read-only parallel agents generally do not need separate worktrees.

Do not create a worktree for every ordinary task. Diff size and task duration alone are not reasons for workspace isolation.

After parallel writes are combined, run integration validation on the combined state rather than trusting each isolated result independently.

## Permissions, Sandboxes, And Hooks

Prefer deterministic controls over repeated warning prose.

Examples:

- deny or ask before dangerous shell patterns;
- restrict write access to the needed workspace;
- limit network access when the task does not need it;
- block secrets or generated local state from commits;
- run format/lint/test checks after relevant writes;
- protect production/deploy/publish/history operations behind explicit permissions.

Low-risk authorized work should remain fluid. High-impact real-state actions should become explicit at the actual risk boundary.

Hooks are useful for deterministic checks. Do not use them to recreate a verbose approval workflow around harmless actions.

## Search And Code Navigation

Use the lightest navigation method that finds the relevant surface reliably:

- native repository search;
- symbol/reference search;
- semantic navigation;
- targeted grep/ripgrep;
- language-server/index tools.

Prefer targeted retrieval over reading entire repositories into context.

Semantic tools may help large codebases, but they do not justify broad edits or bypass repository scope.

## Context And Session Management

Do not introduce another mandatory context taxonomy.

Default rule:

> start with the task, relevant code, tests, and durable repository invariants; retrieve deeper context only when needed.

Use compaction, summaries, retrieval, skills, and handoffs to preserve useful information without keeping every historical detail active.

A context-management tool is valuable only if it reduces reruns or irrelevant tokens without hiding requirements, failures, or important decisions.

## Runtime And Outcome Observability

Make important behavior easy for an agent to observe directly when practical.

Useful capabilities include:

- one-command test/build targets;
- predictable local startup commands;
- readable error output;
- logs and metrics that expose relevant state without secrets;
- CLI/API smoke paths;
- browser/UI inspection for visual behavior;
- deterministic generated artifacts that can be checked.

If agents repeatedly need to guess whether something worked, improving observability may be more valuable than adding prompt detail.

## MCP And External Tools

External tool connections expand both capability and trust surface.

Use least privilege:

- connect only services needed for the task;
- prefer read-only access for exploration;
- avoid broad filesystem/network/write permissions by default;
- keep credentials and active local connection config out of the repository;
- verify what a tool can read/write before relying on it for sensitive work.

Third-party MCP servers, plugins, extensions, and agent packages should be treated like software dependencies, not harmless prompt text.

## Background And Recurring Automation

Automate repeated bounded work when a clear trigger/cadence and useful output exist.

Good candidates include:

- documentation drift checks;
- dependency/CI monitoring;
- stale issue triage;
- recurring quality checks;
- bounded maintenance tasks.

Avoid autonomous background code changes with unclear ownership, weak validation, or unlimited recurrence.

Recurring agents consume compute/tokens even when their output is low-value. Keep cadence and scope proportional to the actual need.

## Output Compression

Compression can be useful for noisy shell exploration.

- Do not compress away details needed to diagnose failures.
- Preserve raw or reproducible evidence for important validation failures, security work, release readiness, and high-impact audits.
- Token savings are useful only when they do not create reruns or ambiguity.

A compression tool is an optimization, not evidence by itself.

## Local Configuration

Prefer user/global configuration for reusable agent tools when project-local state is unnecessary.

Project-local agent config is exception-only and should remain untracked unless the task explicitly asks for a sanitized, intentional repository configuration.

Never commit credentials, auth files, generated agent state, personal paths, active private connection config, or provider secrets.

## Choosing A Tool

Ask:

1. Does it save meaningful work, context, elapsed time, or risk on this task?
2. Is the capability already available natively?
3. Does it require broader permissions than the task needs?
4. Can failures and side effects still be inspected clearly?
5. Does it create repository-local state or long-term maintenance cost?
6. Will coordination/configuration cost exceed the benefit?

If the tool adds more process than it removes, do not use it.

## Harness Feedback

When the same agent friction recurs, improve the harness instead of permanently expanding prompts.

Examples:

- repeated wrong test command -> stable script/target;
- repeated architecture violation -> structural test/lint rule;
- repeated risky command -> permission/hook;
- repeated specialized procedure -> focused skill;
- repeated missing knowledge -> discoverable documentation;
- one-off instruction -> task prompt.

Do not optimize the harness for hypothetical failures. Use observed recurrence, meaningful risk, or clear repeated cost as the signal.

## Environment Bootstrap

Do not make environment bootstrap a mandatory pre-implementation block.

Install/configure a tool only when the current task benefits from it or when the user explicitly requested environment setup. Verify installations before relying on them, and report user-level configuration changes only when they matter.
