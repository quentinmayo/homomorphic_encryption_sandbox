from __future__ import annotations

import pytest

from he_sandbox.experiments.graph.ckks_graph import (
    encrypted_neighbor_score,
    plaintext_neighbor_score,
)


def test_graph_scores_within_tolerance() -> None:
    adjacency = [
        [0.0, 0.8, 0.2],
        [0.5, 0.0, 0.5],
        [0.2, 0.6, 0.0],
    ]
    node_weights = [2.0, 1.0, 3.0]

    plain_scores = plaintext_neighbor_score(adjacency, node_weights)
    enc_scores = encrypted_neighbor_score(adjacency, node_weights)

    assert len(enc_scores) == len(plain_scores)
    for enc_val, plain_val in zip(enc_scores, plain_scores, strict=True):
        assert enc_val == pytest.approx(plain_val, abs=1e-3)
