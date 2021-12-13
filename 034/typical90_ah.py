# https://atcoder.jp/contests/typical90/tasks/typical90_ah

from typing import List, DefaultDict
from collections import defaultdict

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, K: int, A: List[int]):
    x = 0
    y = 0
    es: DefaultDict[int, int] = defaultdict(int)
    sumes = 0
    result = 0
    
    while y < N:

        while y < N:
            e = A[y]
            if es[e] == 0:
                if sumes < K:
                    es[e] = 1
                    sumes += 1
                else:
                    break
            else:
                es[e] += 1
            y += 1

        #print("S", x, y, sumes, es)

        result = max(result, y - x)

        while x < y:
            e = A[x]
            x += 1
            if es[e] > 1:
                es[e] -= 1
            else:
                es[e] = 0
                sumes -= 1
                break

        #print("E", x, y, sumes, es)

    print(result)


solve(N, K, A)
