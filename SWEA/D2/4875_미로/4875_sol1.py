import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    maze = [input() for _ in range(n)]
    check = [[False]*n for _ in range(n)]

    x = -1
    y = -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                x = i
                y = j

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def go(x, y):
        res = 0
        check[x][y] = True
        if maze[x][y] == '3':
            return 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not check[nx][ny]:
                if maze[nx][ny] == '0':
                    res = go(nx, ny)
                    if res == 1:
                        return res
                elif maze[nx][ny] == '3':
                    return 1

        return res


    if x < 0 or y < 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, go(x, y)))
