# https://atcoder.jp/contests/typical90/tasks/typical90_bn

from typing import List

N = int(input())
LR = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, LR: List[List[int]]):
    result = 0
    for i in range(N - 1):
        a0, a1 = LR[i]
        for j in range(i + 1, N):
            b0, b1 = LR[j]
            b = (a1 - a0 + 1) * (b1 - b0 + 1)
            a = 0
            for k in range(b0, b1 + 1):
                c = 0
                if a1 > k:
                    c = a1 - max(a0 - 1, k)
                a += c
            result += a / b
    print(result)


solve(N, LR)
