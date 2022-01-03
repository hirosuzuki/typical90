# https://atcoder.jp/contests/typical90/tasks/typical90_br

from typing import List

N = int(input())
XY = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, XY: List[List[int]]):
    x0 = sorted(x for x, y in XY)[N // 2]
    y0 = sorted(y for x, y in XY)[N // 2]
    result = sum(abs(x - x0) + abs(y - y0) for x, y in XY)
    print(result)


solve(N, XY)
