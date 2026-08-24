#!/usr/bin/env python3
"""Binomial simulation demo for IB Math (probability / distributions).

Teacher pause points are in comments below. Projection-friendly defaults.
"""

from __future__ import annotations

import argparse

import numpy as np

# Teacher pause points:
# 1) Before running: "What should the histogram look like if n=20, p=0.5?"
# 2) After first plot: "What changes if p becomes 0.1?"
# 3) "How is this different from the binomial probability formula for a single k?"


def simulate(n: int, p: float, trials: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.binomial(n=n, p=p, size=trials)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=20, help="number of Bernoulli trials")
    parser.add_argument("--p", type=float, default=0.5, help="success probability")
    parser.add_argument("--trials", type=int, default=5000, help="simulation size")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument(
        "--save",
        type=str,
        default="",
        help="optional path to save figure instead of showing it",
    )
    args = parser.parse_args()

    data = simulate(args.n, args.p, args.trials, args.seed)

    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover
        raise SystemExit(
            "matplotlib is required. Install with: python3 -m pip install matplotlib numpy"
        ) from exc

    fig, ax = plt.subplots(figsize=(10, 6))
    bins = np.arange(-0.5, args.n + 1.5, 1)
    ax.hist(data, bins=bins, density=True, color="#1A47B8", edgecolor="white", alpha=0.9)
    ax.set_title(
        f"Binomial simulation: n={args.n}, p={args.p}, trials={args.trials}",
        fontsize=16,
        pad=12,
    )
    ax.set_xlabel("Number of successes", fontsize=14)
    ax.set_ylabel("Relative frequency", fontsize=14)
    ax.tick_params(labelsize=12)
    ax.set_xticks(range(0, args.n + 1, max(1, args.n // 10)))
    fig.tight_layout()

    if args.save:
        fig.savefig(args.save, dpi=150)
        print(f"Saved {args.save}")
    else:
        print("Close the plot window to exit.")
        plt.show()


if __name__ == "__main__":
    main()
