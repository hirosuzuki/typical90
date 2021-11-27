# https://atcoder.jp/contests/typical90/tasks/typical90_q

from typing import List

N, M = [int(x) for x in input().split()]
LR = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, LR: List[List[int]]):
    if M > 1000:
        return

    r = 0

    for i in range(M):
        for j in range(i + 1, M):
            l1, r1 = LR[i]
            l2, r2 = LR[j]
            if ((l1 < l2 < r1) and (not (l1 <= r2 <= r1))) or ((l1 < r2 < r1) and (not (l1 <= l2 <= r1))):
                r += 1
    
    print(r)


solve(N, M, LR)
