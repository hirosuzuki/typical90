# https://atcoder.jp/contests/typical90/tasks/typical90_d

from typing import List

H, W = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for _ in range(H)]


def solve(H: int, W: int, A: List[List[int]]):
    ht = [sum(row) for row in A]
    wt = [sum(row) for row in zip(*A)]
    for y in range(H):
        for x in range(W):
            print(wt[x] + ht[y] - A[y][x], end=" ")
        print()


solve(H, W, A)
