import sys
# 리스트를 이용해 queue를 쓰면 시간초과가 발생하여 deque을 사용한다.
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    # 이중 for 문 list comprehension
    # lands = [[i, j] for j in range(m) for i in range(n) if grid[i][j] == 'L']

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    steps = [[0 for j in range(m)] for i in range(n)]

    def bfs(q):
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 'L':
                        if steps[nx][ny] == 0:
                            steps[nx][ny] = steps[x][y] + 1
                            q.append([nx, ny])

    # 땅에서부터 물에 대한 최단거리를 찾으면 시간 초과가 발생한다.
    # 그래서 물에서 출발하여 각 땅에 대한 최단거리를 찾아 시간을 단축한다.
    q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'W':
                q.append([i, j])
    bfs(q)
    cnt = 0
    for i in range(n):
        for j in range(m):
            cnt += steps[i][j]

    print('#{} {}'.format(tc, cnt))
