# https://atcoder.jp/contests/typical90/tasks/typical90_v

from math import gcd

A, B, C = [int(x) for x in input().split()]


def solve(A: int, B: int, C: int):
    g = gcd(gcd(A, B), C)
    result = (A // g) - 1 + (B // g) - 1 + (C // g) - 1
    print(result)


solve(A, B, C)
