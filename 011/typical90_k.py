# https://atcoder.jp/contests/typical90/tasks/typical90_k

from typing import List, Dict, DefaultDict
from collections import defaultdict

N = int(input())
DCS = [[int(e) for e in input().split()] for _ in range(N)]


def solve(N: int, DCS: List[List[int]]):

    if N > 8:
        raise

    dcs = sorted(DCS, key=lambda x: x[0])

    result = 0
    for i in range(2**N):
        p = 0
        r = 0
        for j in range(N):
            if i & (1 << (N - 1 - j)):
                if p + dcs[j][1] <= dcs[j][0]:
                    p += dcs[j][1]
                    r += dcs[j][2]
        result = max(result, r)

    print(result)


def solve1(N: int, DCS: List[List[int]]):

    dcs = sorted(DCS, key=lambda x: x[0])

    rs: DefaultDict[int, int] = defaultdict(int)
    rs[0] = 0
    for d, c, s in dcs:
        nrs: DefaultDict[int, int] = defaultdict(int)
        for k, v in rs.items():
            nrs[k] = v
            if k + c <= d:
                nrs[k + c] = max(nrs[k + c], nrs[k] + s)
        rs = nrs

    result = max(v for v in rs.values())
    print(result)


def solve2(N: int, DCS: List[List[int]]):

    dcs = sorted(DCS, key=lambda x: x[0])
    dmax = max(d for d, c, s in dcs)

    rs = [0] * (dmax + 1)
    for d, c, s in dcs:
        nrs = [0] * (dmax + 1)
        for j in range(dmax + 1):
            if c <= j <= d:
                nrs[j] = max(rs[j], rs[j - c] + s)
            else:
                nrs[j] = rs[j]
        rs = nrs

    result = max(v for v in rs)
    print(result)


solve2(N, DCS)
