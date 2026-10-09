"""Run walkthroughs in fresh kernels from both supported working directories."""

from pathlib import Path
import sys

from jupyter_client import KernelManager
import nbformat
from nbclient import NotebookClient
import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("notebook_name", [
    "01_salary_bfv_walkthrough.ipynb",
    "02_graph_ckks_walkthrough.ipynb",
])
@pytest.mark.parametrize("working_directory", [".", "notebooks"])
def test_notebook_executes(notebook_name: str, working_directory: str) -> None:
    notebook = nbformat.read(REPO_ROOT / "notebooks" / notebook_name, as_version=4)
    # Use the test environment, regardless of the user's registered kernels.
    manager = KernelManager(kernel_name="python3")
    manager.kernel_spec.argv = [
        sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}",
    ]
    client = NotebookClient(
        notebook,
        km=manager,
        timeout=120,
        resources={"metadata": {"path": str(REPO_ROOT / working_directory)}},
    )
    # Explicit cleanup also applies when an externally supplied manager is used.
    client.execute(cleanup_kc=True)
