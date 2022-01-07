# https://atcoder.jp/contests/typical90/tasks/typical90_bw

N = int(input())


def solve(N: int):
    x = N

    r = 1
    i = 2
    while i * i <= x:
        if x % i == 0:
            r += 1
            x = x // i
        else:
            i += 1

    result = 0
    while r >= 2:
        r = (r + 1) // 2
        result += 1

    print(result)


solve(N)
