# https://atcoder.jp/contests/typical90/tasks/typical90_ar

from typing import List

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
TXY = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, Q: int, A: List[int], TXY: List[List[int]]):
    offset = 0
    for t, x, y in TXY:
        if t == 1:
            A[(x - 1 + offset) % N], A[(y - 1 + offset) % N] = A[(y - 1 + offset) % N], A[(x - 1 + offset) % N]
        elif t == 2:
            offset -= 1
        elif t == 3:
            print(A[(x - 1 + offset) % N])


solve(N, Q, A, TXY)
