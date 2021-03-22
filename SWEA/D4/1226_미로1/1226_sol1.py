import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_case = int(input())
    n = 16
    maze = [list(input()) for _ in range(n)]
    sx, sy = -1, -1
    ex, ey = -1, -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                sx, sy = i, j
            elif maze[i][j] == '3':
                ex, ey = i, j

    visited = [[0 for i in range(n)] for j in range(n)]
    q = [[sx, sy]]
    visited[sx][sy] = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != '1':
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

    print('#{} {}'.format(tc, visited[ex][ey]))

