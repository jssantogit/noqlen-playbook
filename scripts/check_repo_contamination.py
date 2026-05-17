#!/usr/bin/env python3
"""Check tracked files for repository contamination risks."""

from pathlib import Path
import re
import subprocess
import sys


FORBIDDEN_PATH_PATTERNS = [
    re.compile(r"(^|/)\.opencode(/|$)"),
    re.compile(r"(^|/)\.serena(/|$)"),
    re.compile(r"(^|/)\.mcp(/|$)"),
    re.compile(r"(^|/)\.claude(/|$)"),
    re.compile(r"(^|/)\.cursor(/|$)"),
    re.compile(r"(^|/)\.windsurf(/|$)"),
    re.compile(r"(^|/)\.clinerules(/|$)"),
    re.compile(r"(^|/)\.kilocode(/|$)"),
    re.compile(r"(^|/)\.skills(/|$)"),
    re.compile(r"(^|/)\.agent-state(/|$)", re.IGNORECASE),
    re.compile(r"(^|/)agent-state(/|$)", re.IGNORECASE),
    re.compile(r"(^|/)tool-state(/|$)", re.IGNORECASE),
    re.compile(r"(^|/)(generated[-_.]?)?agent[-_.]?state(/|$)", re.IGNORECASE),
    re.compile(r"(^|/)opencode\.json$"),
    re.compile(r"(^|/)opencode\.jsonc$"),
    re.compile(r"(^|/)\.mcp\.json$", re.IGNORECASE),
    re.compile(r"(^|/)mcp\.json$", re.IGNORECASE),
    re.compile(r"(^|/)mcp[-_.]?config\.(json|yaml|yml|toml)$", re.IGNORECASE),
    re.compile(r"(^|/)serena_config\.(json|yaml|yml)$", re.IGNORECASE),
    re.compile(r"(^|/)agent[-_.]?settings\.(json|yaml|yml|toml)$", re.IGNORECASE),
    re.compile(r"(^|/)RTK\.md$"),
    re.compile(r"(^|/)context-mode.*\.(db|sqlite|sqlite3)$", re.IGNORECASE),
    re.compile(r"(^|/)\.env(\..*)?$"),
    re.compile(r"(^|/)auth\.json$", re.IGNORECASE),
    re.compile(r"(^|/)credentials\.json$"),
    re.compile(r"(^|/)\.secrets(/|$)?"),
    re.compile(r"(^|/)(provider|model|llm)[-_.]?(auth|credentials)\.(json|yaml|yml|toml)$", re.IGNORECASE),
    re.compile(r"(^|/).*(agent|tool|session).*(log|dump)\.(txt|log|json)$", re.IGNORECASE),
    re.compile(r"(^|/)site(/|$)"),
    re.compile(r"^docs/development(/|$)"),
    re.compile(r"audit-report", re.IGNORECASE),
    re.compile(r"model-routing", re.IGNORECASE),
    re.compile(r"/(Users|home)/[^/]+/"),
    re.compile(r"(Music|iTunes|Media Library|Plex|foobar2000)", re.IGNORECASE),
]

SUSPICIOUS_CONTENT_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA |)PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|access[_-]?token|secret[_-]?key|client[_-]?secret)\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
    re.compile(r"(?i)\"(access_token|refresh_token|id_token|client_secret)\"\s*:\s*\"[^\"]{12,}\""),
    re.compile(r"(?i)(github|ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+/=-]{20,}"),
    re.compile(r"/(Users|home)/[^/\s]+/"),
    re.compile(r"(?i)/(music|itunes|media library)/[^\n]+"),
    re.compile(r"(?i)https://[^\s]+/(share|session)/[A-Za-z0-9_-]{12,}"),
    re.compile(r"(?i)(fingerprint|acoustid|chromaprint)\s*[:=]\s*['\"]?[A-Za-z0-9+/=]{24,}"),
]

ALLOWED_EXAMPLE_SUFFIXES = (".example.json", ".example.jsonc", ".example.md")

CONTENT_ALLOWLIST = {"scripts/check_repo_contamination.py"}


def is_sanitized_example(path: str) -> bool:
    return path.startswith("examples/tooling/") and path.endswith(ALLOWED_EXAMPLE_SUFFIXES)


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [line for line in result.stdout.splitlines() if line]


def check_paths(paths: list[str]) -> list[str]:
    failures = []
    for path in paths:
        if is_sanitized_example(path):
            continue
        for pattern in FORBIDDEN_PATH_PATTERNS:
            if pattern.search(path):
                failures.append(f"{path} matches {pattern.pattern}")
    return failures


def check_content(paths: list[str]) -> list[str]:
    failures = []
    for path in paths:
        if path in CONTENT_ALLOWLIST:
            continue
        file_path = Path(path)
        if not file_path.is_file():
            continue
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pattern in SUSPICIOUS_CONTENT_PATTERNS:
                if pattern.search(line):
                    failures.append(f"{path}:{line_no} matches {pattern.pattern}")
    return failures


def main() -> int:
    try:
        paths = tracked_files()
    except subprocess.CalledProcessError as exc:
        print("FAIL: could not inspect tracked files with git ls-files.")
        print(exc.stderr.strip())
        return 1

    path_failures = check_paths(paths)
    content_failures = check_content(paths)

    if path_failures:
        print("Forbidden tracked paths:")
        for failure in path_failures:
            print(f"- {failure}")

    if content_failures:
        print("Suspicious tracked content:")
        for failure in content_failures:
            print(f"- {failure}")

    if path_failures or content_failures:
        print("FAIL: repository contamination check failed.")
        return 1

    print("PASS: no tracked repository contamination detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
