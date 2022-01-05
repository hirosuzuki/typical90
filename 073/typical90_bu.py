# https://atcoder.jp/contests/typical90/tasks/typical90_bu

from typing import List, DefaultDict, Set
from collections import defaultdict

N = int(input())
C = input().split()
AB = [[int(x) for x in input().split()] for _ in range(N - 1)]


def solve(N: int, C: List[str], AB: List[List[int]]):
    M = 10**9+7
    ds: DefaultDict[int, Set[int]] = defaultdict(set)
    for a, b in AB:
        ds[a].add(b)
        ds[b].add(a)
    cs = [False] * (N + 1)
    dp: List[List[int]] = [[0] * 3 for _ in range(N + 1)]

    def dfs(n: int):
        cs[n] = True
        v0 = 1
        v1 = 1
        v2 = 1
        for d in ds[n]:
            if cs[d] is False:
                dfs(d)
                v0 = v0 * (dp[d][0] + dp[d][2]) % M
                v1 = v1 * (dp[d][1] + dp[d][2]) % M
                v2 = v2 * (dp[d][0] + dp[d][1] + 2 * dp[d][2]) % M
        if C[n - 1] == "a":
            dp[n][0] = v0
            dp[n][2] = (v2 - v0) % M
        else:  # == "b"
            dp[n][1] = v1
            dp[n][2] = (v2 - v1) % M

    dfs(1)
    print(dp[1][2])


solve(N, C, AB)
