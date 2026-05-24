from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from he_sandbox.experiments.graph.ckks_graph import (
    encrypted_neighbor_score,
    plaintext_neighbor_score,
)


def main() -> None:
    adjacency = [
        [0.0, 0.8, 0.2],
        [0.5, 0.0, 0.5],
        [0.2, 0.6, 0.0],
    ]
    node_weights = [2.0, 1.0, 3.0]

    plain_scores = plaintext_neighbor_score(adjacency, node_weights)
    enc_scores = encrypted_neighbor_score(adjacency, node_weights)

    print("Graph experiment (CKKS)")
    print(f"Plain scores: {plain_scores}")
    print(f"Encrypted scores: {enc_scores}")


if __name__ == "__main__":
    main()
