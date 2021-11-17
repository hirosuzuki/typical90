# https://atcoder.jp/contests/typical90/tasks/typical90_f
# https://twitter.com/e869120/status/1378840212449595393

from typing import List

N, K = [int(e) for e in input().split()]
S = input()

def solve(N: int, K: int, S: str):
    cn = 26
    cs: List[List[int]] = [[N] * N for _ in range(cn)]
    for i in range(N):
        cs[ord(S[N - i - 1]) - ord("a")][N - i - 1] = N - i - 1
        if i < N - 1:
            for j in range(cn):
                cs[j][N - i - 2] = cs[j][N - i - 1]
    r = ""
    p = 0
    for i in range(K):
        l = K - i - 1
        for j in range(cn):
            if cs[j][p] <= N - 1 - l:
                p = cs[j][p] + 1
                r += chr(ord("a") + j)
                break

    print(r)
    

solve(N, K, S)
