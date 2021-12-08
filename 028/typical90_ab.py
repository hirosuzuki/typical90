# https://atcoder.jp/contests/typical90/tasks/typical90_ab

from typing import List

N = int(input())
LR = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, LR: List[List[int]]):
    M = 1000
    cs = [[0] * (M + 1) for _ in range(M + 1)]
    for lx, ly, rx, ry in LR:
        cs[ly][lx] += 1
        cs[ry][lx] -= 1
        cs[ly][rx] -= 1
        cs[ry][rx] += 1

    for y in range(M + 1):
        for x in range(1, M + 1):
            cs[y][x] += cs[y][x - 1]

    for x in range(M + 1):
        for y in range(1, M + 1):
            cs[y][x] += cs[y - 1][x]

    rs = [0] * (N + 1)

    for y in range(M + 1):
        for x in range(M + 1):
            rs[cs[y][x]] += 1

    for i in range(1, N + 1):
        print(rs[i])


solve(N, LR)
