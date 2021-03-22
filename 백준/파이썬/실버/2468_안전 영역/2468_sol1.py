n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

height = set()
for i in range(n):
    for j in range(n):
        height.add(a[i][j])
height.add(0)


def func(check, x, y, rain):
    q = [[x, y]]
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] > rain and not check[nx][ny]:
                    check[nx][ny] = True
                    q.append([nx, ny])


ans = 0
for rain in height:
    check = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > rain and not check[i][j]:
                check[i][j] = True
                func(check, i, j, rain)
                cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)

