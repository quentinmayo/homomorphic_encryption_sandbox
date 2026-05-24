"""Simple timing helper for experiment steps."""

from __future__ import annotations

import time
from contextlib import contextmanager
from dataclasses import dataclass


@dataclass
class TimedStep:
    name: str
    seconds: float


@contextmanager
def timed(step_name: str):
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"{step_name}: {elapsed:.6f}s")
