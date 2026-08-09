# Tooling

Tooling is an optional acceleration layer. It is **not a step in the Noqlen workflow** and normal tasks do not declare a Tool Mode.

The workflow remains:

```text
Inspect -> Implement -> Verify -> Review
```

Use tools when they reduce real work without hiding evidence or expanding permissions unnecessarily.

## OpenCode Native Capabilities

Prefer native repository inspection, search, plan/build modes, permissions, and read-only agents before adding extra tooling.

Use executable permissions for risky actions when possible. A denied destructive command is a stronger guardrail than repeating "do not run this command" in every prompt.

Keep sharing disabled or manual for real private work unless explicitly intended.

## Serena

Serena can help with semantic navigation when a repository is large enough that symbol-level inspection saves context.

- Start read-only when possible.
- Editing must stay inside the task's actual scope.
- Do not use semantic editing as justification for broad refactors.
- Keep active local Serena state untracked.

## RTK / Command Output Compression

Compression can be useful for noisy shell exploration.

- Do not compress away the details needed to diagnose failures.
- Preserve raw or reproducible evidence for important validation failures, security work, release readiness, and high-risk audits.
- Token savings are useful only when they do not create reruns or ambiguity.

## Context Routing / Long Sessions

Context-routing tools may help long sessions, but they should not create another mandatory context taxonomy.

Default rule:

> start with the task, relevant code, tests, and durable repository invariants; load broader context only when needed.

## Terse Status Tools

Concise status output is fine for temporary conversational updates. Do not let terse formatting remove requirements, failure detail, security findings, or decisions that need to be reviewable.

## Local Configuration

Prefer user/global configuration for reusable agent tools.

Project-local agent config is exception-only and should remain untracked unless the task explicitly asks for a sanitized example.

Never commit credentials, auth files, generated agent state, personal paths, active MCP config, or provider secrets.

## Choosing A Tool

Ask:

1. Does it save meaningful time/context on this task?
2. Does it require broader permissions than the task needs?
3. Can failures still be inspected clearly?
4. Does it create repository-local state or configuration?
5. Is the same result already available through native capabilities?

If the tool adds more process than it removes, do not use it.

## Environment Bootstrap

Do not make environment bootstrap a mandatory pre-implementation block.

Install/configure a tool only when the current task benefits from it or when the user explicitly requested environment setup. Verify installations before relying on them, and report user-level configuration changes when they matter.
