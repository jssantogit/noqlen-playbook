# Optimized Development Environment

The Noqlen optimized development environment is an optional setup for AI-assisted projects. It reduces wasted context, improves semantic navigation, compresses noisy command output, and gives agents better codebase awareness.

Tooling is an optimization layer. It must not replace scoped blocks, specs, validation, audits, handoffs, repository hygiene, or human review.

## Purpose

Use this environment when a project handoff asks an implementation agent to prepare the development environment before coding. The agent should install or configure approved tools, verify them, and report what changed before product implementation starts.

## Default Recommended Stack

1. OpenCode native capabilities.
2. Serena read-only.
3. RTK for shell-heavy blocks.
4. Context Mode as a pilot for long sessions.
5. Caveman disabled by default.

## Installation Matrix

| Tool | Purpose | Install scope | Required? | Default status |
|---|---|---|---|---|
| OpenCode native | Agent execution controls | user/global | baseline | explicit permissions |
| Serena | Semantic code navigation/editing | user/global | recommended | read-only first |
| RTK | Command output compression | user/global | recommended | shell-heavy blocks |
| Context Mode | Context/output routing | user/global | pilot | validate OpenCode support locally |
| Caveman | terse conversation/status | user/global | optional | disabled by default |

## Scope Rules

- Global/user-level setup is preferred for reusable tooling.
- Project-level config is allowed only when explicitly approved.
- Local generated config or state must remain untracked unless explicitly approved and sanitized.
- Environment bootstrap is separate from product implementation.
- Tooling must be declared in the block as Environment Mode and Tool Mode.

## OpenCode Native Setup

- Prefer global/user-level config.
- Use project-local config only by explicit exception.
- Keep share disabled or manual for real Noqlen work.
- Make permissions explicit for risky operations such as shell commands, file writes, network access, commits, pushes, and destructive actions.
- Avoid committing `opencode.json` or `.opencode/`.
- Provider credentials and auth files must never be committed.

## Serena Installation

Serena is the recommended first accelerator for semantic navigation and codebase understanding. Start read-only.

Official warning: do not install Serena via an MCP/plugin marketplace. Use the official Quick Start path.

```bash
uv tool install -p 3.13 serena-agent@latest --prerelease=allow
serena --help
```

Rules:

- Start with read-only usage.
- Enable editing only inside explicit allowed files.
- Do not allow broad refactors unless the block scope explicitly asks.
- Do not commit `.serena/`.
- If Serena creates project-local state, report it and keep it untracked unless explicitly approved.
- Prefer project Serena data outside the repo when possible.

## RTK Installation

```bash
# macOS/Linux option 1
brew install rtk

# macOS/Linux option 2
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh

# Cargo option
cargo install --git https://github.com/rtk-ai/rtk

# Verify
rtk --version
rtk gain
```

OpenCode setup:

```bash
rtk init -g --opencode
rtk init --show
```

Rules:

- Prefer user/global setup.
- Do not commit generated local config.
- Preserve raw failure evidence when relevant.
- Compressed output is not audit proof.
- Raw failure evidence is required when relevant.
- If RTK compresses command output, final audit must still mention whether raw output was available.
- On Windows, prefer WSL for full hook support.
- Internal Noqlen policy: telemetry is explicit opt-in only.
- Verify RTK telemetry/privacy state during pilot.

## Context Mode Installation

Prerequisites:

- Node.js >= 22.5 or Bun, when applicable.
- OpenCode installed when configuring OpenCode integration.

Global install:

```bash
npm install -g context-mode
```

OpenCode support should be treated as pilot/partial unless validated in the current environment.

Preferred configuration:

- Prefer global config: `~/.config/opencode/opencode.json`.
- Avoid project-level `opencode.json` unless explicitly approved.
- Never commit `opencode.json` by accident.

Sanitized global config example:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "context-mode": {
      "type": "local",
      "command": ["context-mode"],
      "environment": {
        "CONTEXT_MODE_IDLE_TIMEOUT_MS": "900000"
      }
    }
  },
  "plugin": ["context-mode"]
}
```

Verification:

```bash
context-mode doctor
```

In an OpenCode session:

```text
ctx stats
```

Rules:

- Context Mode may route or sandbox tool output.
- It cannot be the only source of audit evidence.
- Do not commit generated routing files unless explicitly sanitized and intended as documentation.
- Prefer global/user-level configuration.
- Do not overwrite an existing global OpenCode config without backing it up or showing the diff first.
- Do not commit active Context Mode config/state.
- Watch for process or lifecycle issues in long OpenCode sessions.
- Context Mode output is not final audit evidence by itself.

## Caveman / Terse-Output Installation

Caveman / terse-output tooling is optional only and disabled by default in Noqlen.

Default cross-agent installer:

```bash
# macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash

# Windows PowerShell 5.1+
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```

Rules:

- Disabled by default in Noqlen.
- Allowed only for temporary status/conversation compression.
- Forbidden for specs, ADRs, audit reports, handoffs, release notes, public docs, and architectural decisions.
- Prefer compact but complete wording over meme-style compressed language.
- Do not use Caveman to rewrite Noqlen Playbook docs, AGENTS.md, specs, ADRs, or handoffs.
- Caveman can be documented as optional, but should not become part of the default Noqlen development mode.

## MCP Safety

- Prefer local stdio transport by default.
- Remote HTTP/SSE MCP servers require explicit exception and security review.
- Do not expose local MCP servers to untrusted networks.
- Do not commit MCP credentials or active configs.
- Use sanitized `.example.*` files only.

## Safety Policy

- No destructive setup without explicit user confirmation.
- No secrets in configs.
- No personal paths in committed files.
- No real music library paths.
- No lyrics, fingerprints, or private data.
- No generated local tool folders committed.
- No agent-local config committed unless explicitly approved and sanitized.
- Prefer global config for tools.
- Project docs may mention install commands, but must not store user-specific config.
- Any tool that modifies user-level config must report exactly what was changed.
- Any install failure must be reported; the agent must not pretend setup succeeded.
