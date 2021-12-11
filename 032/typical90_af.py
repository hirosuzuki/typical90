# https://atcoder.jp/contests/typical90/tasks/typical90_af

from typing import List
from itertools import permutations

N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]
M = int(input())
XY = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, A: List[List[int]], M: int, XY: List[List[int]]):

    L = 10**10
    ngs = set((x - 1, y - 1) for x, y in XY)

    result = L

    for e in permutations(range(N)):

        if any((e[i], e[i + 1]) in ngs for i in range(N - 1)):
            continue

        if any((e[i + 1], e[i]) in ngs for i in range(N - 1)):
            continue

        r = sum(A[e[i]][i] for i in range(N))

        result = min(result, r)

    if result >= L:
        result = -1

    print(result)


solve(N, A, M, XY)
