import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                start_x = i
                start_y = j
            elif maze[i][j] == '3':
                end_x = i
                end_y = j

    q = [[start_x, start_y]]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cnt = 0
    visited = [[0 for i in range(n)] for j in range(n)]
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == '3':
                    visited[nx][ny] = visited[x][y]
                    break
                if maze[nx][ny] == '0' and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    print('#{} {}'.format(tc, visited[end_x][end_y]))
