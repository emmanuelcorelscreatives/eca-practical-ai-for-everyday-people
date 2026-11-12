"""Exact, offline checks for Academy lesson 85; Python 3, no dependencies."""
from fractions import Fraction

def percentage(parts, total):
    if total <= 0:
        raise ValueError("total must be positive")
    return Fraction(parts, total) * 100

if __name__ == "__main__":
    assert percentage(25, 100) == 25
    assert percentage(40, 100) == 40
    assert Fraction(50, 10) == 5
    assert percentage(15, 20) == 75
    print("PASS: 25/100=25%; 40/100=40%; 50/10=5; 15/20*100=75%")
