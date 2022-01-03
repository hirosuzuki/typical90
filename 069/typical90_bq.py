# https://atcoder.jp/contests/typical90/tasks/typical90_bq

N, K = [int(x) for x in input().split()]


def solve(N: int, K: int):
    M = 10**9+7
    if N == 1:
        return K % M
    if N == 2:
        return K * (K - 1) % M
    if K < 3:
        return 0
    result = K * (K - 1) % M * pow((K - 2), (N - 2), M) % M
    return result

print(solve(N, K))
