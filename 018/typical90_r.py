# https://atcoder.jp/contests/typical90/tasks/typical90_r

from typing import List
from math import pi, cos, sin, atan2, sqrt

T = int(input())
L, X, Y = [int(x) for x in input().split()]
Q = int(input())
E = [int(input()) for _ in range(Q)]


def solve(T: int, L: int, X: int, Y: int, Q: int, E: List[int]):
    for i in E:
        t = 2 * pi * i / T
        y = -sin(t) * L / 2
        z = L / 2 - cos(t) * L / 2
        d = sqrt(X**2 + (Y - y)**2)
        r = atan2(z, d) * 180 / pi
        # print(i, t, y, z, d, r)
        print(r)


solve(T, L, X, Y, Q, E)
