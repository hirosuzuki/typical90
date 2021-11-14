from typing import Dict, Set

N = int(input())

def solve(N: int):

    if N % 2 == 1:
        return

    rs: Dict[str, Set[str]] = {}
    rs[0] = set([])
    rs[2] = set(["()"])

    for i in range(4, N + 1, 2):
        rs[i] = set([])
        for es1 in rs[i - 2]:
            rs[i].add("(" + es1 + ")")
        for j in range(2, i, 2):
            for es1 in rs[j]:
                for es2 in rs[i - j]:
                    rs[i].add(es1 + es2)

    for x in sorted(rs[N]):
        print(x)

solve(N)