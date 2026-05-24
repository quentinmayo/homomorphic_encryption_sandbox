"""BFV salary experiment: encrypted total compensation computation."""

from __future__ import annotations

from typing import Any

from he_sandbox.config import create_bfv_context
from he_sandbox.experiments.salary.scenario import EmployeeComp


def plaintext_totals(employees: list[EmployeeComp]) -> tuple[list[int], int]:
    """Compute per-employee total comp and full payroll in plaintext."""
    per_employee = [emp.salary + emp.company_contribution for emp in employees]
    return per_employee, sum(per_employee)


def encrypt_totals(employees: list[EmployeeComp]) -> tuple[Any, Any]:
    """Encrypt compensation totals and return ciphertext objects."""
    try:
        import tenseal as ts
    except ImportError as exc:
        raise RuntimeError(
            "TenSEAL is required for encrypted salary computations."
        ) from exc

    context = create_bfv_context()

    salaries = [emp.salary for emp in employees]
    contributions = [emp.company_contribution for emp in employees]

    enc_salary = ts.bfv_vector(context, salaries)
    enc_contrib = ts.bfv_vector(context, contributions)

    enc_per_employee = enc_salary + enc_contrib
    enc_company_total = enc_per_employee.sum()

    return enc_per_employee, enc_company_total


def decrypt_totals(enc_per_employee: Any, enc_company_total: Any) -> tuple[list[int], int]:
    """Decrypt encrypted totals back into plaintext values."""
    per_employee_total = [int(v) for v in enc_per_employee.decrypt()]
    company_total = int(enc_company_total.decrypt()[0])
    return per_employee_total, company_total


def encrypted_totals(employees: list[EmployeeComp]) -> tuple[list[int], int]:
    """Compute compensation totals using BFV and return decrypted results."""
    enc_per_employee, enc_company_total = encrypt_totals(employees)
    per_employee_total, company_total = decrypt_totals(enc_per_employee, enc_company_total)

    return per_employee_total, company_total
