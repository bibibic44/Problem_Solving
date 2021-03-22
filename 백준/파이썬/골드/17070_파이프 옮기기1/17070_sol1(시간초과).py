# import sys
# 시간초과 발생

# 가로(오른쪽), 세로(아래쪽), 오른쪽 대각선 아래
dx = [0, 1, 1]
dy = [1, 0, 1]

def is_check(house, x, y, n, p):
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


def func(house, x, y, n, p):
    if x == n-1 and y == n-1:
        return 1
    cnt = 0

    for k in range(3):
        # 가로 방향에서는 세로로 이동 불가
        if p == 0 and k == 1:
            continue
        # 세로 방향에서는 가로로 이동 불가
        elif p == 1 and k == 0:
            continue
        nx = x + dx[k]
        ny = y + dy[k]
        if is_check(house, nx, ny, n, k):
            tmp = func(house, nx, ny, n, k)
            cnt += tmp
    return cnt

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
# house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# # input test
# print(n, house, type(house[0][0]))

print(func(house, 0, 1, n, 0))
