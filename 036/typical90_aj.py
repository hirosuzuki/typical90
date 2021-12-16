# https://atcoder.jp/contests/typical90/tasks/typical90_aj

from typing import List

N, Q = [int(x) for x in input().split()]
XY = [[int(x) for x in input().split()] for _ in range(N)]
QS = [int(input()) for _ in range(Q)]


def solve(N: int, Q: int, XY: List[List[int]], QS: List[int]):
    rxy = [(x - y, x + y) for x, y in XY]
    max_rx = max(rx for rx, ry in rxy)
    max_ry = max(ry for rx, ry in rxy)
    min_rx = min(rx for rx, ry in rxy)
    min_ry = min(ry for rx, ry in rxy)
    for n in QS:
        x, y = rxy[n - 1]
        r = max(abs(max_rx - x), abs(min_rx - x),
                abs(max_ry - y), abs(min_ry - y))
        print(r)


solve(N, Q, XY, QS)
