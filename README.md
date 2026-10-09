# Homomorphic Encryption Sandbox

This repository is a Python sandbox for exploring homomorphic encryption workflows with separate experiments:

- Salary computation with encrypted values (BFV, exact integer arithmetic).
- Graph computation with encrypted vectors (CKKS, approximate arithmetic).

## Quick Start

Use Python 3.10 or newer with a TenSEAL wheel available for your platform.
Python 3.12 with TenSEAL 0.3.18 has been verified on Apple Silicon macOS.
Run the following commands from the repository root.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If you use another compatible Python version, substitute its executable for
`python3.12`. Keep the virtual environment active for the commands below.

## Project Layout

- `src/he_sandbox/experiments/salary/` - salary and company contribution scenario.
- `src/he_sandbox/experiments/graph/` - encrypted graph score computation.
- `tests/` - correctness checks against plaintext baselines.
- `scripts/` - simple entry points to run each experiment.

## Run Experiments

```powershell
python scripts/run_salary.py
python scripts/run_graph.py
python scripts/run_all.py
```

The salary example should return `[80000, 99000, 109000]` and a company total
of `288000`. The graph example should return approximately `[1.4, 2.5, 1.0]`;
small differences are expected with CKKS.

## Interactive Notebooks

```bash
python -m jupyterlab notebooks
```

See [the notebook guide](notebooks/README.md) for the two walkthroughs.

## Run Tests

```powershell
python -m pytest -q
```

Tests execute real encryption and both notebooks from the repository root and
the notebook directory. Install all requirements first; missing TenSEAL is a
test failure, so a passing run verifies the encrypted computations actually ran.

## Git Hooks (Auto-Clear Notebook Outputs)

This repo includes Git hooks that automatically clear Jupyter notebook outputs:

- `pre-commit`: clears outputs from staged `*.ipynb` files and re-stages them.
- `pre-push`: blocks push if any tracked `*.ipynb` still contains outputs.

Set up hooks once per clone. On Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup_git_hooks.ps1
```

On macOS / Linux:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit .githooks/pre-push
```

## Notes

- BFV is used for exact integer math in salary totals.
- The demo's BFV plaintext modulus is `1032193`; signed results must stay
  between `-516096` and `516096` to avoid modular wraparound. Larger payrolls
  require different parameters or a different representation.
- CKKS is used for approximate vector math in graph scoring.
- This project is for learning and local experimentation, not production key management.
