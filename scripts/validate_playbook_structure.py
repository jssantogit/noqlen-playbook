#!/usr/bin/env python3
"""Validate the required Noqlen Playbook repository structure."""

from pathlib import Path
import sys


REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    ".gitignore",
    "docs/00-overview.md",
    "docs/01-ai-development-workflow.md",
    "docs/02-context-system.md",
    "docs/03-block-based-development.md",
    "docs/04-specs-and-adrs.md",
    "docs/05-opencode-workflow.md",
    "docs/06-audit-workflow.md",
    "docs/07-testing-and-validation.md",
    "docs/08-repo-hygiene.md",
    "docs/09-app-development-workflow.md",
    "docs/10-release-workflow.md",
    "docs/11-future-ai-workflows.md",
    "docs/12-local-ecosystem-study.md",
    "docs/13-workflow-retrofit-patterns.md",
    "templates/context/current.md",
    "templates/context/handoff.md",
    "templates/context/delta-summary.md",
    "templates/context/audit-summary.md",
    "templates/specs/requirements.md",
    "templates/specs/design.md",
    "templates/specs/tasks.md",
    "templates/specs/review.md",
    "templates/adr/adr-template.md",
    "templates/prompts/opencode-plan-block.md",
    "templates/prompts/opencode-implement-block.md",
    "templates/prompts/opencode-audit-block.md",
    "templates/prompts/opencode-fix-audit-findings.md",
    "templates/prompts/opencode-prepare-release.md",
    "templates/prompts/chatgpt-planning-session.md",
    "templates/prompts/opencode-study-local-repos.md",
    "templates/prompts/opencode-retrofit-existing-repo.md",
    "templates/prompts/opencode-extract-workflow-lessons.md",
    "templates/github/pull_request_template.md",
    "templates/github/issue_feature.md",
    "templates/github/issue_bug.md",
    "templates/github/issue_audit.md",
    "examples/aria-core/block-workflow-example.md",
    "examples/aria-core/audit-example.md",
    "examples/aria-core/handoff-example.md",
    "examples/forge-core/workflow-retrospective.md",
    "examples/forge-core/retrofit-example.md",
    "examples/forge-core/block-example.md",
    "examples/flux/workflow-retrospective.md",
    "examples/flux/retrofit-example.md",
    "examples/flux/block-example.md",
    "examples/anchor/workflow-retrospective.md",
    "examples/anchor/retrofit-example.md",
    "examples/anchor/block-example.md",
    "examples/app-shell/app-feature-spec-example.md",
    "examples/app-shell/ui-agent-prompt-example.md",
    "examples/future-ai/agent-boundary-example.md",
    "examples/future-ai/data-safety-example.md",
    "scripts/check_repo_contamination.py",
    "scripts/validate_playbook_structure.py",
]

REQUIRED_DIRS = [
    "docs",
    "templates",
    "templates/context",
    "templates/specs",
    "templates/adr",
    "templates/prompts",
    "templates/github",
    "examples",
    "examples/aria-core",
    "examples/forge-core",
    "examples/flux",
    "examples/anchor",
    "examples/app-shell",
    "examples/future-ai",
    "scripts",
]


def main() -> int:
    root = Path.cwd()
    missing_dirs = [path for path in REQUIRED_DIRS if not (root / path).is_dir()]
    missing_files = [path for path in REQUIRED_FILES if not (root / path).is_file()]

    if missing_dirs:
        print("Missing directories:")
        for path in missing_dirs:
            print(f"- {path}")

    if missing_files:
        print("Missing files:")
        for path in missing_files:
            print(f"- {path}")

    if missing_dirs or missing_files:
        print("FAIL: playbook structure is incomplete.")
        return 1

    print("PASS: playbook structure is complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
