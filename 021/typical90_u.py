# https://atcoder.jp/contests/typical90/tasks/typical90_u

from sys import setrecursionlimit
from typing import List, DefaultDict, Set
from collections import defaultdict

N, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]

setrecursionlimit(200000)

def solve(N: int, M: int, AB: List[List[int]]):

    ds: DefaultDict[int, Set[int]] = defaultdict(set)
    ds_rev: DefaultDict[int, Set[int]] = defaultdict(set)
    for a, b in AB:
        ds[a].add(b)
        ds_rev[b].add(a)

    visited: List[bool] = [False] * (N + 1)
    orders: List[int] = []

    def dfs(x: int):
        visited[x] = True
        for y in ds[x]:
            if not visited[y]:
                dfs(y)
        orders.append(x)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)

    visited = [False] * (N + 1)

    count = 0

    def dfs_rev(x: int):
        nonlocal count
        visited[x] = True
        count += 1
        for y in ds_rev[x]:
            if not visited[y]:
                dfs_rev(y)

    result = 0

    for i in orders[::-1]:
        if not visited[i]:
            count = 0
            dfs_rev(i)
            result += count * (count - 1) // 2

    print(result)

solve(N, M, AB)
