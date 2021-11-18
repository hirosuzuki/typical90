# https://atcoder.jp/contests/typical90/tasks/typical90_g
# https://twitter.com/e869120/status/1379565222541680644/photo/1

from typing import List
from bisect import bisect_left

N = int(input())
A = [int(e) for e in input().split()]
Q = int(input())
B = [int(input()) for e in range(Q)]


def solve(N: int, A: List[int], Q: int, B: List[int]):
    cs = [-10**10] + sorted(A) + [10**10]
    for j in range(Q):
        i = bisect_left(cs, B[j])
        r = min(abs(cs[i - 1] - B[j]), abs(cs[i] - B[j]))
        print(r)


solve(N, A, Q, B)
