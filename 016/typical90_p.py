# https://atcoder.jp/contests/typical90/tasks/typical90_p

from math import gcd

N = int(input())
A, B, C = [int(x) for x in input().split()]

def solve(N: int, A: int, B: int, C: int):
    result = 10**10
    A, B, C = sorted([A, B, C])
    for c in range(N // C, -1, -1):
        x = N - c * C
        for b in range(x // B, -1, -1):
            y = x - b * B
            if y % A == 0:
                r = y // A + b + c
                result = min(result, r)
                break
    print(result)

solve(N, A, B, C)
