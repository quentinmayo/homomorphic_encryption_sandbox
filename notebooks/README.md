# Notebooks

These walkthroughs run the sandbox experiments and check their results:

- `01_salary_bfv_walkthrough.ipynb` encrypts salaries and contributions, inspects
  serialized ciphertext, and checks that decrypted totals match plaintext exactly.
- `02_graph_ckks_walkthrough.ipynb` encrypts graph node weights and checks neighbor
  scores against plaintext with an absolute tolerance of `1e-3`.

Install the root `requirements.txt` in your virtual environment, activate it, then
launch JupyterLab from the repository root:

```bash
python -m jupyterlab notebooks
```

Select the virtual environment's Python kernel and run all cells in order. Both
notebooks support a kernel working directory of either the repository root or
`notebooks/`.

`python -m pytest -q` executes both walkthroughs in fresh kernels without saving
outputs to the source files. Keep committed notebooks free of outputs; the Git
hooks described in the root README automate cleanup.
