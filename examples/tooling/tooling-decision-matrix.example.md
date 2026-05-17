# Tooling Decision Matrix Example

This is a sanitized example.

| Situation | Recommended Tool Mode | Notes |
| --- | --- | --- |
| Small docs edit | `none` or `native` | Tooling is optional. |
| Unknown code symbols | `serena-ro` | Read-only semantic navigation first. |
| Scoped semantic edit | `serena-edit` | Allowed files must be explicit. |
| Shell-heavy validation | `rtk` | Preserve raw failures and audit evidence. |
| Long session or large outputs | `context-mode` | Pilot and validate OpenCode support locally. |
| Temporary status compression | `caveman-limited` | Disabled by default and forbidden for formal docs. |
| Multiple accelerators | `combo` | List each tool and evidence rule. |

Tooling cannot bypass specs, validation, audits, handoffs, or repo hygiene.
