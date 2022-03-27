from math import factorial
"""


Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
https://projecteuler.net/problem=15
"""

def A(n, k):
    return factorial(n) / factorial(n - k)


def C(n, k):
    return int(A(n, k) / factorial(k))


def main():
    """use la combinatoire"""
    n = 20
    return C(2 * n, n)


if __name__ == "__main__":
    print(main())
