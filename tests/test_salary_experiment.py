from __future__ import annotations

import importlib.util

import pytest

from he_sandbox.experiments.salary.bfv_salary import encrypted_totals, plaintext_totals
from he_sandbox.experiments.salary.scenario import sample_employees


tenseal_installed = importlib.util.find_spec("tenseal") is not None


@pytest.mark.skipif(not tenseal_installed, reason="TenSEAL not installed")
def test_salary_totals_match_plaintext() -> None:
    employees = sample_employees()

    plain_per_employee, plain_total = plaintext_totals(employees)
    enc_per_employee, enc_total = encrypted_totals(employees)

    assert enc_per_employee == plain_per_employee
    assert enc_total == plain_total
