# https://atcoder.jp/contests/typical90/tasks/typical90_ae

from typing import List, Set

N = int(input())
W = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


def solve(N: int, W: List[int], B: List[int]):
    L = 50 + 50*(50+1)//2 + 2
    # L = 20
    grundy = [[0] * L for _ in range(51)]

    def mex(xs: Set[int]) -> int:
        x = 0
        while True:
            if x not in xs:
                break
            x += 1
        return x

    for j in range(2, L):
        grundy[0][j] = mex(set(grundy[0][j-j//2:j]))

    for i in range(1, 51):
        for j in range(0, L):
            if j + i >= L:
                continue
            s = set(grundy[i][j-j//2:j]) | set([grundy[i-1][j+i]])
            grundy[i][j] = mex(s)

    r = 0
    for w, b in zip(W, B):
        r ^= grundy[w][b]

    if r == 0:
        print("Second")
    else:
        print("First")


solve(N, W, B)
