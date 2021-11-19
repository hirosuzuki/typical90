# https://atcoder.jp/contests/typical90/tasks/typical90_h

N = int(input())
S = input()


def solve(N: int, S: str):
    M = 10**9+7
    T = "atcoder"
    rs = [1] + [0] * len(T)
    for c in S:
        if c in T:
            i = T.index(c)
            rs[i + 1] = (rs[i + 1] + rs[i]) % M

    print(rs[-1])


solve(N, S)
