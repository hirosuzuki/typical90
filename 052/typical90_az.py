# https://atcoder.jp/contests/typical90/tasks/typical90_az

from typing import List

N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, A: List[List[int]]):
    M = 10**9+7
    xs = A[0]
    for rs in A[1:]:
        xs = [sum((xs[i] * rs[j]) % M for j in range(6)) % M for i in range(6)]
    result = sum(xs) % M
    print(result)


solve(N, A)
