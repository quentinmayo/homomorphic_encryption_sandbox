# Homomorphic Encryption Sandbox

This repository is a Python sandbox for exploring homomorphic encryption workflows with separate experiments:

- Salary computation with encrypted values (BFV, exact integer arithmetic).
- Graph computation with encrypted vectors (CKKS, approximate arithmetic).

## Quick Start (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

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

## Run Tests

```powershell
pytest -q
```

## Git Hooks (Auto-Clear Notebook Outputs)

This repo includes Git hooks that automatically clear Jupyter notebook outputs:

- `pre-commit`: clears outputs from staged `*.ipynb` files and re-stages them.
- `pre-push`: blocks push if any tracked `*.ipynb` still contains outputs.

Set up hooks once per clone:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup_git_hooks.ps1
```

## Notes

- BFV is used for exact integer math in salary totals.
- CKKS is used for approximate vector math in graph scoring.
- This project is for learning and local experimentation, not production key management.
