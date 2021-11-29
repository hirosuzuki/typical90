# https://atcoder.jp/contests/typical90/tasks/typical90_t

A, B, C = [int(x) for x in input().split()]


def solve(A: int, B: int, C: int):
    if A < C ** B:
        print("Yes")
    else:
        print("No")


solve(A, B, C)
