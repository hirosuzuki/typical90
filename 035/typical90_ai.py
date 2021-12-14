# https://atcoder.jp/contests/typical90/tasks/typical90_ai

from sys import setrecursionlimit
from typing import Dict, List, DefaultDict, Set, Dict
from collections import defaultdict

setrecursionlimit(200000)

N = int(input())
AB = [[int(x) for x in input().split()] for _ in range(N - 1)]
Q = int(input())
KV = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, AB: List[List[int]], Q: int, KV: List[List[int]]):

    if N > 5000 or Q > 5000:
        return

    rs: DefaultDict[int, Set[int]] = defaultdict(set)
    for a, b in AB:
        rs[a].add(b)
        rs[b].add(a)

    def calc(m: int, qs: Set[int]) -> int:
        cs: Dict[int, int] = {}
        result = 0

        def bfs(n: int) -> int:
            nonlocal result
            r = 1 if (n in qs) else 0
            cs[n] = r
            for b in rs[n]:
                if b not in cs:
                    r += bfs(b)
            cs[n] = r
            if 0 < r < m:
                result += 1
            return r

        bfs(1)

        return result

    for xs in KV:
        print(calc(xs[0], set(xs[1:])))


solve(N, AB, Q, KV)
