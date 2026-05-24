from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_script(path: Path, cwd: Path) -> None:
    subprocess.run([sys.executable, str(path)], check=True, cwd=str(cwd))


def main() -> None:
    scripts_dir = Path(__file__).resolve().parent
    repo_root = scripts_dir.parent
    run_script(scripts_dir / "run_salary.py", repo_root)
    run_script(scripts_dir / "run_graph.py", repo_root)


if __name__ == "__main__":
    main()
