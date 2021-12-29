# https://atcoder.jp/contests/typical90/tasks/typical90_bi

from typing import List

N = int(input())
TX = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, TX: List[List[int]]):
    ts: List[int] = []
    bs: List[int] = []
    for t, x in TX:
        if t == 1:
            ts.append(x)
        elif t == 2:
            bs.append(x)
        elif t == 3:
            if x <= len(ts):
                print(ts[-x])
            else:
                print(bs[x - len(ts) - 1])


solve(N, TX)
