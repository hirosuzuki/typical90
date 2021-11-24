# https://atcoder.jp/contests/typical90/tasks/typical90_n

from typing import List

N = int(input())
A = [int(e) for e in input().split()]
B = [int(e) for e in input().split()]


def solve(N: int, A: List[int], B: List[int]):
    xs1 = sorted(A)
    xs2 = sorted(B)
    result = 0
    for a, b, in zip(xs1, xs2):
        result += abs(a - b)
    print(result)


solve(N, A, B)
