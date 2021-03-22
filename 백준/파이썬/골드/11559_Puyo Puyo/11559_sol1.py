n, m = 12, 6
field = [list(input()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(x, y, check):
    q = []
    q.append([x, y])
    flag = False
    cnt = 1
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == field[x][y]:
                if check[nx][ny] == 0:
                    check[nx][ny] = 1
                    q.append([nx, ny])
                    cnt += 1
                    if cnt >= 4:
                        flag = True
    if flag:
        for i in range(n):
            for j in range(m):
                if check[i][j] != 0:
                    field[i][j] = '.'

    return flag


def gravity(field):
    for j in range(m):
        # 아래부터 검사
        for i in range(n-1, 0, -1):
            if field[i][j] == '.' and field[i-1][j] != '.':
                idx = i
                # 빈 칸이 있을 경우 빈 칸으로 한 칸씩 끌어내린다.
                while True:
                    if idx >= n or field[idx][j] != '.':
                        break
                    field[idx][j] = field[idx - 1][j]
                    field[idx - 1][j] = '.'
                    idx += 1


ans = 0

while True:
    is_flag = False
    for i in range(n):
        for j in range(m):
            check = [[0 for _ in range(m)] for _ in range(n)]
            if field[i][j] != '.':
                check[i][j] = 1
                tmp = bfs(i, j, check)
                # 한 번이라도 터진 그룹이 있다면 턴이 끝난 다음 중력이 작용해야 한다.
                if tmp:
                    is_flag = True
    # 한 번에 터뜨릴 수 있는 그룹을 전부 터뜨리고 나야 한 턴이 종료된다.
    # 한 턴이 종료될 때마다 중력이 작용해 블록들이 빈 공간으로 내려온다.
    if is_flag:
        ans += 1
        gravity(field)
    # 터질 수 있는 그룹이 더 이상 없어서 연쇄가 끝났다면 종료한다.
    else:
        break

print(ans)

