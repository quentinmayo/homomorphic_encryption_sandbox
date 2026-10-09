from __future__ import annotations

from he_sandbox.experiments.salary.bfv_salary import encrypted_totals, plaintext_totals
from he_sandbox.experiments.salary.scenario import sample_employees


def test_salary_totals_match_plaintext() -> None:
    employees = sample_employees()

    plain_per_employee, plain_total = plaintext_totals(employees)
    enc_per_employee, enc_total = encrypted_totals(employees)

    assert enc_per_employee == plain_per_employee
    assert enc_total == plain_total
