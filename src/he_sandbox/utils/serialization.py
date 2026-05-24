"""Helpers for serializing TenSEAL contexts and ciphertexts."""

from __future__ import annotations

from pathlib import Path


def write_bytes(path: Path, payload: bytes) -> None:
    """Persist bytes to disk, creating parent folders when needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def read_bytes(path: Path) -> bytes:
    """Load bytes from disk."""
    return path.read_bytes()
