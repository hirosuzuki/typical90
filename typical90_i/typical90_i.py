# https://atcoder.jp/contests/typical90/tasks/typical90_i

from typing import List
from math import atan2, pi
from bisect import bisect_left

N = int(input())
XY = [[int(e) for e in input().split()] for _ in range(N)]

def solve(N: int, XY: List[List[int]]):

    def calc(i: int):
        angles: List[float] = []
        for j in range(N):
            if i != j:
                dx = XY[j][0] - XY[i][0]
                dy = XY[j][1] - XY[i][1]
                angle = atan2(dy, dx) * 180 / pi
                angles.append(angle)
        axs = list(angles)
        for a in angles:
            if a < 0:
                axs.append(a + 360)
            else:
                axs.append(a - 360)
        def c360(x: float) -> float:
            if x < 0:
                x += 360
            if x > 180:
                x = 360 - x
            return x
        axs.sort()
        r = 0
        for a in angles:
            rs: List[float] = []
            r1 = bisect_left(axs, a - 180)
            if 0 <= r1 < len(axs):
                rs.append(axs[r1])
            if 0 <= r1 - 1< len(axs):
                rs.append(axs[r1 - 1])
            r2 = bisect_left(axs, a + 180)
            if 0 <= r2 < len(axs):
                rs.append(axs[r2])
            if 0 <= r2 - 1< len(axs):
                rs.append(axs[r2 - 1])
            crs = [c360(x - a) for x in rs]
            #print(axs, a, r1, r2, rs, crs)
            r = max(max(crs), r)
        return r

    result = 0
    for i in range(N):
        result = max(calc(i), result)
    print(result)

solve(N, XY)
