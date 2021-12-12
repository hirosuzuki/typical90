# https://atcoder.jp/contests/typical90/tasks/typical90_ag

H, W = [int(x) for x in input().split()]


def solve(H: int, W: int):
    if H == 1 or W == 1:
        result = H * W
    else:
        result = ((H + 1) // 2) * ((W + 1) // 2)
    print(result)


solve(H, W)
