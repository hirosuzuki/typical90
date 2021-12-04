# https://atcoder.jp/contests/typical90/tasks/typical90_y

from sys import setrecursionlimit

setrecursionlimit(100000)

N, B = [int(x) for x in input().split()]


def solve(N: int, B: int):

    result = 0

    def dfs(s: str, n: int):
        nonlocal result
        k = 1
        for c in s:
            k *= int(c)
        y = B + k
        if y <= N and "".join(sorted(str(y))) == s:
            result += 1

        if len(s) == 11:
            return
        for i in range(n, 10):
            dfs(s + str(i), i)

    for i in range(0, 10):
        dfs(str(i), i)

    print(result)


solve(N, B)
