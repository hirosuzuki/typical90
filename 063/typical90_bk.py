# https://atcoder.jp/contests/typical90/tasks/typical90_bk

from typing import List, DefaultDict
from collections import defaultdict

H, W = [int(x) for x in input().split()]
P = [[int(x) for x in input().split()] for _ in range(H)]


def solve(H: int, W: int, P: List[List[int]]):
    result = 0
    for n in range(1, 2**H):
        cs: DefaultDict[int, int] = defaultdict(int)
        for i in range(W):
            rs = [P[j][i] for j in range(H) if (1 << j) & n]
            if all(rs[0] == k for k in rs[1:]):
                cs[rs[0]] += len(rs)
        r = max(cs.values()) if cs else 0
        # print(n, cs, r)
        result = max(result, r)
    print(result)


solve(H, W, P)
