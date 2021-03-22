# 백준 참고, DP 사용
import sys
n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 3차원 리스트, d[x][y][dir]이며, dir은 파이프의 방향이다.
d = [[[-1]*3 for j in range(n)] for i in range(n)]


def func(x, y, p):
    if x == n-1 and y == n-1:
        return 1

    cnt = d[x][y][p]
    if cnt != -1:
        return cnt
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

    d[x][y][p] = cnt
    return cnt


print(func(0, 1, 0))
