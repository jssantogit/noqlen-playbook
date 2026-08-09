# Tooling

Tooling is an optional acceleration layer. It is **not a step in the Noqlen workflow** and normal tasks do not declare a Tool Mode.

The workflow remains:

```text
Inspect -> Implement -> Verify -> Review
```

Use tools only when they reduce real work, context waste, elapsed time, or risk without hiding evidence or expanding permissions unnecessarily.

## Capabilities Before Brands

Organize the environment around durable capabilities, not today's preferred product names:

- search/navigation;
- skills/procedures;
- subagents/parallel execution;
- isolated workspaces/worktrees;
- permissions/sandboxes/hooks;
- test/runtime observability;
- context retrieval/compaction;
- MCP/external tools;
- background automation.

Specific tools are replaceable implementations of these capabilities.

## Native Capabilities First

Prefer capabilities already provided by the active agent/runtime before installing another layer.

Add a tool only when it provides measurable value the native environment does not already provide well. If configuration or coordination costs more than the capability saves, skip it.

## Skills And Reusable Procedures

Use a skill/procedure for a workflow that repeats, benefits from reusable instructions, and is too detailed for `AGENTS.md`.

Keep skills focused and load deeper instructions/scripts/references only when needed.

Choose placement by the type of problem, not by a fixed hierarchy:

- durable invariant -> `AGENTS.md`;
- repeated procedure -> skill;
- deterministic constraint -> code/tooling when practical and cheaper to maintain;
- durable knowledge -> discoverable docs;
- one-off guidance -> task prompt.

Use the lightest durable mechanism that solves the actual recurring problem. Do not create a skill, hook, lint rule, or script merely because the category exists.

## Subagents And Workspaces

**Default to one capable agent.** Delegate only when separate context or independent execution materially reduces elapsed time, context interference, or residual risk.

Good uses include parallel read-only investigation, focused specialist review, independent failure analysis, and independent implementation units with stable boundaries.

Keep one coordinator responsible for scope, integration, and final verification.

Do not create a fixed `planner -> coder -> tester -> reviewer` pipeline for routine work, and avoid delegation when workers depend heavily on the same rapidly changing shared state.

Concurrent writers should use isolated workspaces/worktrees/branches when interference is possible. Read-only parallel agents generally do not need them. Re-validate the combined state after integration.

## Permissions, Sandboxes, And Hooks

Prefer deterministic controls over repeated warning prose when a rule is genuinely mechanical.

Examples:

- restrict write/network scope;
- ask/deny dangerous commands;
- block secrets or generated state from commits;
- run relevant lint/test checks;
- protect production, publish, deploy, and history actions behind explicit permissions.

Low-risk authorized work should remain fluid. Add hooks or approval boundaries only where they reduce a concrete failure mode and are cheaper than the failures they prevent.

## Search, Context, And Observability

Prefer targeted retrieval over loading entire repositories into context. Use native search, symbol/reference search, semantic navigation, grep, indexes, or language-server tools as appropriate.

Do not create another mandatory context taxonomy. Start with the task, relevant code, tests, and durable invariants; retrieve deeper context only when needed.

Use compaction, summaries, skills, and handoffs only when they reduce irrelevant context without hiding requirements or failures.

Make important behavior easy for agents to observe when practical: stable test/build commands, predictable startup, readable errors, sanitized logs/metrics, CLI/API smoke paths, UI inspection, and checkable artifacts.

If agents repeatedly need to guess whether something worked, improving observability is usually better than adding prompt detail.

## MCP, Plugins, And Supply Chain

External tools expand both capability and trust surface.

- connect only what the task needs;
- prefer read-only access for exploration;
- minimize filesystem/network/write permissions;
- keep credentials and active private config out of the repository;
- review untrusted or newly adopted third-party skills, plugins, MCP servers, and agent packages before relying on them;
- re-review when provenance, version, permissions, or behavior changes materially;
- pin/version durable dependencies when reproducibility matters.

Do **not** re-audit an unchanged, already-approved dependency on every routine use. Treat adoption and material updates as the trust boundary.

Treat external agent tooling as software dependencies, not harmless prompt text.

## Background Automation

Automate repeated bounded work only when a clear trigger/cadence and useful output exist, such as CI monitoring, documentation drift checks, dependency checks, stale issue triage, or bounded maintenance.

Avoid autonomous recurring code changes with unclear ownership or weak validation. Recurring agents consume compute/tokens even when their output is low-value.

## Output Compression

Compression is useful for noisy exploration only when it does not hide failures or force reruns.

Preserve raw or reproducible evidence for important validation failures, security work, release readiness, and high-impact audits.

## Harness Feedback

When the same friction recurs, choose the lightest durable fix that matches the cause:

- deterministic failure -> test/lint/script/permission/hook when cheap to maintain;
- repeated procedure -> focused skill;
- repeated missing knowledge -> discoverable docs;
- one-off instruction -> prompt.

Do not optimize for hypothetical failures. Recurrence, meaningful risk, or clear repeated cost is the signal.

## Local Configuration

Prefer user/global configuration when project-local state is unnecessary. Keep credentials, auth files, generated agent state, personal paths, and active private connection config out of the repository.

## Choosing A Tool

Ask:

1. Does it save meaningful work, context, elapsed time, or risk?
2. Is the capability already available natively?
3. Are permissions no broader than needed?
4. Can failures and side effects still be inspected?
5. Does maintenance/configuration cost exceed the benefit?

If the tool adds more process than it removes, do not use it.

## Environment Bootstrap

Do not make environment bootstrap a mandatory pre-implementation block.

Install/configure a tool only when the current task benefits from it or when the user explicitly requested environment setup. Verify installations before relying on them, and report user-level configuration changes only when they matter.
