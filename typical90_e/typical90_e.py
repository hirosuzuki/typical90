# https://atcoder.jp/contests/typical90/tasks/typical90_e

from typing import List, DefaultDict, Set, Tuple, Deque, Dict
from collections import defaultdict, deque

N, B, K = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]

def solve(N: int, B: int, K: int, C: List[int]):
    M = 10**9+7
    rs = [0] * B
    rs[0] = 1
    for i in range(N):
        nrs = [0] * B
        for x in C:
            for j in range(B):
                ix = (j * 10 + x) % B
                nrs[ix] = (nrs[ix] + rs[j]) % M
        rs = nrs
    print(rs[0])

def solve2(N: int, B: int, K: int, C: List[int]):
    M = 10**9+7
    m = [[0] * B for _ in range(B)]
    print(m)

solve2(N, B, K, C)
