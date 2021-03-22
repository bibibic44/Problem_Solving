def ok(n, m, nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def func(board, x, y, cnt, dx, dy, n, m):
    if cnt == 0:
        return 0

    ans = -1

    # 이동할 방향 선택
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 장애물, 기존에 갔던 길이 아니고 범위를 넘지 않으면 끝까지 이동
        while ok(n, m, nx, ny) and board[nx][ny] == '.':
            cnt -= 1
            board[nx][ny] = '#'
            nx += dx[k]
            ny += dy[k]
        # while문을 탈출했다 = 조건에 위배되었다. ---> 조정
        nx -= dx[k]
        ny -= dy[k]

        # 이동하지 못한 경우는 제외
        if not (nx == x and ny == y):
            # 이동한 자리에서 다시 재귀
            tmp = func(board, nx, ny, cnt, dx, dy, n, m)
            if tmp != -1:
                if ans == -1 or ans > tmp+1:
                    ans = tmp+1

        # 다시 x, y로 back + '#'로 표시한 것도 되돌린다.
        while not (x == nx and y == ny):
            cnt += 1
            board[nx][ny] = '.'
            nx -= dx[k]
            ny -= dy[k]

    return ans


tc = 1

while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    # for i in range(n):
    #     board.append(list(input()))
    board = [list(input()) for _ in range(n)]

    # 좌표
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # 이동 가능한 칸 수 카운트
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                cnt += 1

    # 시작 가능한 지점마다 함수 호출
    ans = -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                # 이미 방문했다는 표시
                board[i][j] = '#'
                # cnt도 한 칸 줄게 된다.
                tmp = func(board, i, j, cnt-1, dx, dy, n, m)
                if tmp != -1:
                    if ans == -1 or ans > tmp:
                        ans = tmp
                board[i][j] = '.'

    print('Case {}: {}'.format(tc, ans))
    tc += 1