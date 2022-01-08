# https://atcoder.jp/contests/typical90/tasks/typical90_bx

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    total = sum(A)
    if total % 10 != 0:
        print("No")
        return
    t = total // 10

    xs = [0]

    for a in A:
        xs.append(xs[-1] + a)
    for a in A:
        xs.append(xs[-1] + a)

    def check(st: int) -> bool:
        n = st + 1
        m = st + N
        while n + 1 < m:
            i = (n + m) // 2
            x = xs[i] - xs[st]
            if x == t:
                return True
            elif x >= t:
                m = i
            else:
                n = i
        i = (n + m) // 2
        return (xs[i] - xs[st]) == t

    for i in range(N):
        if check(i):
            print("Yes")
            return

    print("No")


solve(N, A)
