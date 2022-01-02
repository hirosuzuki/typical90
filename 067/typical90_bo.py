# https://atcoder.jp/contests/typical90/tasks/typical90_bo

N, K = [int(x) for x in input().split()]

def to9(n: int) -> str:
    if n == 0:
        return "0"
    s = ""
    while n:
        n, m = divmod(n, 9)
        s = str(m) + s
    return s

def solve(N: int, K: int):
    result = str(N)
    for _ in range(K):
        s = int(result, 8)
        result = to9(s).replace("8", "5")
    print(result)


solve(N, K)