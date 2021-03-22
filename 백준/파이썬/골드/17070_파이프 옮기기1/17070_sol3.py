import sys

n = int(input())
# house = [list(map(int, input().split())) for _ in range(n)]
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def func(x, y, p):
    if x == n-1 and y == n-1:
        return 1
    cnt = 0

    # 가로 방향
    if p == 0:
        if y+1 < n and house[x][y+1] == 0:
            cnt += func(x, y+1, 0)
        if x+1 < n and y+1 < n and house[x+1][y+1] == 0 and house[x+1][y] == 0 and house[x][y+1] == 0:
            cnt += func(x+1, y+1, 2)
    # 세로 방향
    elif p == 1:
        if x+1 < n and house[x+1][y] == 0:
            cnt += func(x+1, y, 1)
        if x+1 < n and y+1 < n and house[x+1][y+1] == 0 and house[x+1][y] == 0 and house[x][y+1] == 0:
            cnt += func(x+1, y+1, 2)
    # 대각선 방향
    elif p == 2:
        if y+1 < n and house[x][y+1] == 0:
            cnt += func(x, y+1, 0)
        if x+1 < n and house[x+1][y] == 0:
            cnt += func(x+1, y, 1)
        if x+1 < n and y+1 < n and house[x+1][y+1] == 0 and house[x+1][y] == 0 and house[x][y+1] == 0:
            cnt += func(x+1, y+1, 2)

    return cnt


print(func(0, 1, 0))
