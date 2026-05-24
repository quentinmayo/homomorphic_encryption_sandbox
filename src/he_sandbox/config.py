"""Shared TenSEAL context helpers for sandbox experiments."""

from __future__ import annotations

from typing import Any

# BFV parameters for exact integer arithmetic workloads.
BFV_POLY_MODULUS_DEGREE = 4096
BFV_PLAIN_MODULUS = 1032193

# CKKS parameters for approximate vector arithmetic workloads.
CKKS_POLY_MODULUS_DEGREE = 8192
CKKS_COEFF_MOD_BIT_SIZES = [60, 40, 40, 60]
CKKS_GLOBAL_SCALE = 2**40


def create_bfv_context() -> Any:
    """Create a BFV context with generated keys for exact integer operations."""
    try:
        import tenseal as ts
    except ImportError as exc:
        raise RuntimeError(
            "TenSEAL is required for BFV experiments but is not installed in this environment."
        ) from exc

    context = ts.context(
        ts.SCHEME_TYPE.BFV,
        poly_modulus_degree=BFV_POLY_MODULUS_DEGREE,
        plain_modulus=BFV_PLAIN_MODULUS,
    )
    context.generate_galois_keys()
    context.generate_relin_keys()
    return context


def create_ckks_context() -> Any:
    """Create a CKKS context with generated keys for approximate vector operations."""
    try:
        import tenseal as ts
    except ImportError as exc:
        raise RuntimeError(
            "TenSEAL is required for CKKS experiments but is not installed in this environment."
        ) from exc

    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=CKKS_POLY_MODULUS_DEGREE,
        coeff_mod_bit_sizes=CKKS_COEFF_MOD_BIT_SIZES,
    )
    context.global_scale = CKKS_GLOBAL_SCALE
    context.generate_galois_keys()
    context.generate_relin_keys()
    return context
