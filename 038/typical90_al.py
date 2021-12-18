# https://atcoder.jp/contests/typical90/tasks/typical90_al

from math import gcd

A, B = [int(x) for x in input().split()]


def solve(A: int, B: int):
    L = 10**18
    c = gcd(A, B)
    r = A * B // c
    if r > L:
        print("Large")
    else:
        print(r)


solve(A, B)
