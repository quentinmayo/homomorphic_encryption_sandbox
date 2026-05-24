"""Clear Jupyter notebook outputs for cleaner commits."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def _git_paths(args: list[str]) -> list[Path]:
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    paths = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return [Path(path) for path in paths if path.lower().endswith(".ipynb")]


def staged_notebooks() -> list[Path]:
    return _git_paths(["diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "*.ipynb"])


def tracked_notebooks() -> list[Path]:
    return _git_paths(["ls-files", "--", "*.ipynb"])


def clear_outputs(path: Path, write: bool) -> bool:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    changed = False
    for cell in data.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True

    if changed and write:
        with path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
            f.write("\n")

    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--staged", action="store_true", help="Operate on staged notebooks")
    source.add_argument("--tracked", action="store_true", help="Operate on tracked notebooks")
    parser.add_argument("--check", action="store_true", help="Only check; do not modify files")
    parser.add_argument(
        "--restage",
        action="store_true",
        help="Re-stage changed files after write (use with --staged)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        paths = staged_notebooks() if args.staged else tracked_notebooks()
    except subprocess.CalledProcessError as exc:
        print(exc.stderr.strip() or "Failed to query git for notebooks.", file=sys.stderr)
        return 2

    if not paths:
        return 0

    changed_paths: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if clear_outputs(path, write=not args.check):
            changed_paths.append(path)

    if changed_paths and args.restage:
        subprocess.run(["git", "add", "--", *(str(path) for path in changed_paths)], check=True)

    if changed_paths:
        print("Notebook outputs cleared:" if not args.check else "Notebook outputs detected:")
        for path in changed_paths:
            print(f" - {path.as_posix()}")

    if args.check and changed_paths:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
