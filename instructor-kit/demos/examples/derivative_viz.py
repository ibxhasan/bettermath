#!/usr/bin/env python3
"""Derivative visualisation demo for IB Math calculus hooks.

Shows a secant approaching a tangent on y = x^2.
"""

from __future__ import annotations

import argparse

import numpy as np

# Teacher pause points:
# 1) "What does (f(a+h)-f(a))/h represent geometrically?"
# 2) "As h shrinks, what happens to the secant?"
# 3) "What would change for f(x)=x^3 at a negative a?"


def f(x: np.ndarray | float) -> np.ndarray | float:
    return x**2


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=float, default=1.0, help="point of interest")
    parser.add_argument("--h", type=float, default=1.0, help="initial secant step")
    parser.add_argument(
        "--save",
        type=str,
        default="",
        help="optional path to save figure instead of showing it",
    )
    args = parser.parse_args()

    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover
        raise SystemExit(
            "matplotlib is required. Install with: python3 -m pip install matplotlib numpy"
        ) from exc

    a, h = args.a, args.h
    xs = np.linspace(a - 2.5, a + 2.5, 400)
    ys = f(xs)

    secant_slope = (f(a + h) - f(a)) / h
    tangent_slope = 2 * a  # for f(x)=x^2

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xs, ys, color="#1A47B8", lw=2.5, label=r"$y=x^2$")

    # Secant line through a and a+h
    sec_x = np.array([a - 1.5, a + h + 1.5])
    sec_y = f(a) + secant_slope * (sec_x - a)
    ax.plot(sec_x, sec_y, color="#C44545", lw=2, label=f"secant slope ≈ {secant_slope:.3f}")

    # Tangent line
    tan_x = np.array([a - 1.8, a + 1.8])
    tan_y = f(a) + tangent_slope * (tan_x - a)
    ax.plot(tan_x, tan_y, color="#287C78", lw=2, linestyle="--", label=f"tangent slope = {tangent_slope:.3f}")

    ax.scatter([a, a + h], [f(a), f(a + h)], color="black", s=40, zorder=5)
    ax.set_title("Secant → tangent (first principles intuition)", fontsize=16, pad=12)
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("y", fontsize=14)
    ax.tick_params(labelsize=12)
    ax.legend(fontsize=12, loc="upper left")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()

    print(f"a={a}, h={h}, secant={secant_slope:.6f}, derivative={tangent_slope:.6f}")

    if args.save:
        fig.savefig(args.save, dpi=150)
        print(f"Saved {args.save}")
    else:
        print("Close the plot window to exit. Try --h 0.2 or --h 0.05")
        plt.show()


if __name__ == "__main__":
    main()
