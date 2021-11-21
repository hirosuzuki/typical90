# https://atcoder.jp/contests/typical90/tasks/typical90_j

from typing import List

N = int(input())
CP = [[int(e) for e in input().split()] for _ in range(N)]
Q = int(input())
LR = [[int(e) for e in input().split()] for _ in range(Q)]


def solve(N: int, CP: List[List[int]], Q: int, LR: List[List[int]]):
    p1 = [0]
    p2 = [0]

    for c, p in CP:
        p1.append(p1[-1] + p * (c == 1))
        p2.append(p2[-1] + p * (c == 2))

    for l, r in LR:
        print(p1[r] - p1[l - 1], p2[r] - p2[l - 1])


solve(N, CP, Q, LR)
