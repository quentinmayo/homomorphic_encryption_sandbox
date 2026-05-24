"""CKKS graph experiment: encrypted weighted neighbor scoring."""

from __future__ import annotations

from he_sandbox.config import create_ckks_context


def plaintext_neighbor_score(adjacency: list[list[float]], weights: list[float]) -> list[float]:
    """Compute one-step weighted neighbor score in plaintext."""
    scores: list[float] = []
    for row in adjacency:
        scores.append(sum(edge * w for edge, w in zip(row, weights, strict=True)))
    return scores


def encrypted_neighbor_score(adjacency: list[list[float]], weights: list[float]) -> list[float]:
    """Compute weighted neighbor score with encrypted weight vector."""
    try:
        import tenseal as ts
    except ImportError as exc:
        raise RuntimeError(
            "TenSEAL is required for encrypted graph computations."
        ) from exc

    context = create_ckks_context()
    enc_weights = ts.ckks_vector(context, weights)

    decrypted_scores: list[float] = []
    for row in adjacency:
        enc_score = enc_weights.dot(row)
        decrypted_scores.append(float(enc_score.decrypt()[0]))
    return decrypted_scores
