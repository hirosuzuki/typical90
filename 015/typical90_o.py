# https://atcoder.jp/contests/typical90/tasks/typical90_o

N = int(input())

M = 10**9 + 7
L = 100000

Fm = {}
inverseFm = {}
x = 1
for i in range(L + 1):
    Fm[i] = x
    inverseFm[i] = pow(Fm[i], M - 2, M)
    x = x * (i + 1) % M

def C(n, r):
    if n < r:
        return 0
    result = (Fm[n] * inverseFm[r]) % M * inverseFm[n - r] % M
    return result

def solve(N: int):
    for k in range(1, N + 1):
        r = 0
        for a in range(1, N + 1):
            x = N - (k - 1) * (a - 1)
            if x < 0:
                break
            v = C(x, a)
            r = (r + v) % M
        print(r)

solve(N)
