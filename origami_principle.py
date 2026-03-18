"""
Origami Principle: Rational Geometry Through Discrete Folding
"""

import math
from fractions import Fraction

def fold_circle_rational(diameter):
    return Fraction(22, 7) * diameter

def fold_circle_float(diameter):
    return (22/7) * diameter

def main():
    print("=" * 80)
    print("ORIGAMI PRINCIPLE: EXACT RATIONAL GEOMETRY")
    print("=" * 80)
    
    # Single comparison
    diameters = [1, 7, 14, 21, 100]
    print("\n--- SINGLE ITERATION ---")
    for D in diameters:
        exact = fold_circle_rational(D)
        float_val = fold_circle_float(D)
        pi_val = math.pi * D
        error = abs(float_val - pi_val)
        print(f"D={D:3d}: 22/7 exact={str(exact):>10} float={float_val:.15f} π={pi_val:.15f} error={error:.15f}")
    
    # Drift demonstration
    iterations = 10
    exact = Fraction(1, 1)
    float_22_7 = 1.0
    float_pi = 1.0
    
    print("\n--- DRIFT OVER 10 ITERATIONS ---")
    for i in range(1, iterations + 1):
        exact = fold_circle_rational(exact)
        float_22_7 = fold_circle_float(float_22_7)
        float_pi = math.pi * float_pi
        drift = abs(float_22_7 - float_pi)
        print(f"Iter {i:2d}: drift = {drift:.10f}")

if __name__ == "__main__":
    main()