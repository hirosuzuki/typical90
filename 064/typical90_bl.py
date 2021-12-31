# https://atcoder.jp/contests/typical90/tasks/typical90_bl

from typing import List

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
LRV = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, Q: int, A: List[int], LRV: List[List[int]]):
    ds = [y - x for x, y in zip(A, A[1:])]
    result = sum(abs(d) for d in ds)
    for l, r, v in LRV:
        if l >= 2:
            n = ds[l - 2] + v
            result += abs(n) - abs(ds[l - 2])
            ds[l - 2] = n
        if r - 1 < N - 1:
            n = ds[r - 1] - v
            result += abs(n) - abs(ds[r - 1])
            ds[r - 1] = n
        print(result)


solve(N, Q, A, LRV)
