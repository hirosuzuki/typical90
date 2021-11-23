# https://atcoder.jp/contests/typical90/tasks/typical90_m

from typing import List, DefaultDict, Dict
from heapq import heappush, heappop
from collections import defaultdict

N, M = [int(e) for e in input().split()]
ABC = [[int(e) for e in input().split()] for _ in range(M)]


def solve(N: int, M: int, ABC: List[List[int]]):
    ds: DefaultDict[int, Dict[int, int]] = defaultdict(dict)
    for a, b, c in ABC:
        ds[a][b] = c
        ds[b][a] = c

    def calc_distance(ds: DefaultDict[int, Dict[int, int]], S: int) -> Dict[int, int]:
        h = []
        rs: Dict[int, int] = {}

        heappush(h, (0, S))

        while h:
            l, x = heappop(h)
            if x not in rs:
                rs[x] = l
                for y, d in ds[x].items():
                    if y not in rs:
                        heappush(h, (l + d, y))

        return rs

    rs1 = calc_distance(ds, 1)
    rs2 = calc_distance(ds, N)

    for i in range(1, N + 1):
        print(rs1[i] + rs2[i])


solve(N, M, ABC)
