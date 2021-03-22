# is_check 함수를 살리면서 재귀 호출 줄이기
import sys

n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def is_check(x, y, p):
    if 0 <= x < n and 0 <= y < n:
        if p == 0:
            if house[x][y] == 0:
                return True
        elif p == 1:
            if house[x][y] == 0:
                return True
        else:
            if house[x][y] == 0 and house[x-1][y] == 0 and house[x][y-1] == 0:
                return True
    return False


def func(x, y, p):
    if x == n-1 and y == n-1:
        return 1
    cnt = 0

    # 가로 방향
    if p == 0:
        if is_check(x, y+1, 0):
            cnt += func(x, y+1, 0)
        if is_check(x+1, y+1, 2):
            cnt += func(x+1, y+1, 2)
    # 세로 방향
    elif p == 1:
        if is_check(x+1, y, 1):
            cnt += func(x+1, y, 1)
        if is_check(x+1, y+1, 2):
            cnt += func(x+1, y+1, 2)
    # 대각선 방향
    elif p == 2:
        if is_check(x, y+1, 0):
            cnt += func(x, y+1, 0)
        if is_check(x+1, y, 1):
            cnt += func(x+1, y, 1)
        if is_check(x+1, y+1, 2):
            cnt += func(x+1, y+1, 2)

    return cnt


print(func(0, 1, 0))
