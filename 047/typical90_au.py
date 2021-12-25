# https://atcoder.jp/contests/typical90/tasks/typical90_au

from typing import List, Dict

N = int(input())
S = input()
T = input()

ctable: Dict[str, str] = {
    "RR": "R",
    "RB": "G",
    "RG": "B",
    "BR": "G",
    "BB": "B",
    "BG": "R",
    "GR": "B",
    "GB": "R",
    "GG": "G",
}

def solve(N: int, S: str, T: str):
    if N > 2000:
        return
    cs: List[List[str]] = [[" "] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            r = ctable[S[i]+T[j]]
            cs[i][j] = r

    result = 0
    for t in range(1-N, N):
        s = max(-t, 0)
        e = min(N - t, N)
        c1 = cs[s][s + t]
        for i in range(s + 1, e):
            if cs[i][i + t] != c1:
                break
        else:
            result += 1

    print(result)

solve(N, S, T)
