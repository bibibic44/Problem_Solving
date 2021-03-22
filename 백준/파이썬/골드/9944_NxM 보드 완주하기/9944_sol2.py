# 백준 코드
dx = [0,0,1,-1]
dy = [1,-1,0,0]

tc = 1
while True:
    try:
        n, m = map(int,input().split())
    except:
        break
    cnt = 0
    a = [list(input()) for _ in range(n)]
    def go(x, y, cnt):
        ans = -1
        if cnt == 0:
            return 0
        def ok(x, y):
            return 0 <= x < n and 0 <= y < m
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            while ok(nx, ny) and a[nx][ny] == '.':
                a[nx][ny] = '#'
                cnt -= 1
                nx += dx[k]
                ny += dy[k]
            nx -= dx[k]
            ny -= dy[k]
            if not (x == nx and y == ny):
                temp = go(nx, ny, cnt)
                if temp != -1:
                    if ans == -1 or ans > temp+1:
                        ans = temp+1
            while not (x == nx and y == ny):
                a[nx][ny] = '.'
                cnt += 1
                nx -= dx[k]
                ny -= dy[k]
        return ans

    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                cnt += 1
    ans = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                a[i][j] = '#'
                temp = go(i, j, cnt-1)
                if temp != -1:
                    if ans == -1 or ans > temp:
                        ans = temp
                a[i][j] = '.'
    print('Case %d: %d'% (tc, ans))
    tc += 1