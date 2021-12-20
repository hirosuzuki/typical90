# https://atcoder.jp/contests/typical90/tasks/typical90_ap

K = int(input())

def solve(K: int):
    M = 10**9+7
    dp: List[List[int]] = [[0] * 9 for _ in range(K + 1)]
    dp[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, K + 1):
        for j in range(9):
            dp[i][j] = sum(dp[i - k][(j - k) % 9] for k in range(1, 10) if i - k >= 0) % M

    print(dp[K][0])


solve(K)
