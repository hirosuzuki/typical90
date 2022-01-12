# https://atcoder.jp/contests/typical90/tasks/typical90_bz

from typing import List, DefaultDict, Set
from collections import defaultdict

N, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, AB: List[List[int]]):
    ds: DefaultDict[int, Set] = defaultdict(set)
    for a, b in AB:
        ds[a].add(b)
        ds[b].add(a)
    result = 0
    for i in range(1, N + 1):
        xs = [x for x in ds[i] if x < i]
        if len(xs) == 1:
            result += 1
    print(result)


solve(N, M, AB)
