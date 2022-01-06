# https://atcoder.jp/contests/typical90/tasks/typical90_bv

N = int(input())
S = input()


def solve(N: int, S: str):
    result = 0
    for i, c in enumerate(S):
        result += (ord(c) - 97)*(2**i)
    print(result)


solve(N, S)
