# is_check 함수를 살리면서 재귀 호출 줄이기
# is_check 함수를 func 함수 안에 넣어보았다. 하지만 여전히 시간초과 발생
import sys

n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def func(x, y, p):
    def is_check(nx, ny, np):
        if 0 <= nx < n and 0 <= ny < n:
            if np == 0:
                if house[nx][ny] == 0:
                    return True
            elif np == 1:
                if house[nx][ny] == 0:
                    return True
            else:
                if house[nx][ny] == 0 and house[nx - 1][ny] == 0 and house[nx][ny - 1] == 0:
                    return True
        return False

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
