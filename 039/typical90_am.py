# https://atcoder.jp/contests/typical90/tasks/typical90_am

from typing import List, Set, DefaultDict
from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(200000)

N = int(input())
AB = [[int(x) for x in input().split()] for _ in range(N - 1)]


def solve(N: int, AB: List[List[int]]):
    ds: DefaultDict[int, Set[int]] = defaultdict(set)
    for a, b in AB:
        ds[a].add(b)
        ds[b].add(a)

    cs: List[int] = [0] * (N + 1)

    def dfs(n: int) -> int:
        cs[n] = 1
        for d in ds[n]:
            if cs[d] == 0:
                cs[n] += dfs(d)
        return cs[n]

    dfs(1)

    result = sum([cs[i] * (N - cs[i]) for i in range(1, N + 1)])

    print(result)


solve(N, AB)
