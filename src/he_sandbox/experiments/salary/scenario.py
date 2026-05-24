"""Scenario data for salary and company contribution computation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EmployeeComp:
    name: str
    salary: int
    company_contribution: int


def sample_employees() -> list[EmployeeComp]:
    """Return a small deterministic set of employee compensation inputs."""
    return [
        EmployeeComp(name="Ava", salary=72_000, company_contribution=8_000),
        EmployeeComp(name="Noah", salary=88_000, company_contribution=11_000),
        EmployeeComp(name="Liam", salary=95_000, company_contribution=14_000),
    ]
