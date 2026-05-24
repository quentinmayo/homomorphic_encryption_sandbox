from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from he_sandbox.experiments.salary.bfv_salary import encrypted_totals, plaintext_totals
from he_sandbox.experiments.salary.scenario import sample_employees


def main() -> None:
    employees = sample_employees()
    plain_per_employee, plain_total = plaintext_totals(employees)
    enc_per_employee, enc_total = encrypted_totals(employees)

    print("Salary experiment (BFV)")
    print(f"Plain per-employee totals: {plain_per_employee}")
    print(f"Encrypted per-employee totals: {enc_per_employee}")
    print(f"Plain company total: {plain_total}")
    print(f"Encrypted company total: {enc_total}")


if __name__ == "__main__":
    main()
