import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    play = []
    board = [[0]*n for _ in range(n)]
    mid = n // 2
    # 미리 채워져 있는 돌
    board[mid][mid] = board[mid-1][mid-1] = 2
    board[mid][mid-1] = board[mid-1][mid] = 1
    # 돌을 채우자
    for i in range(m):
        r, c, stone = map(int, input().split())
        play.append([c-1, r-1, stone])

    # 8방향
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for i in range(m):
        # 흑돌
        if play[i][2] == 1:
            board[play[i][0]][play[i][1]] = 1
            for k in range(8):
                nx = play[i][0] + dx[k]
                ny = play[i][1] + dy[k]
                while 0 <= nx < n and 0 <= ny < n:
                    # 백돌이 나왔으면 같은 방향으로 이동한다.
                    if board[nx][ny] == 2:
                        nx += dx[k]
                        ny += dy[k]
                        # 흑돌이 나오면 왔던 경로를 되짚어가면서 백돌을 흑돌로(1)로 바꾸어준다.
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                            # while nx != play[i][0] or ny != play[i][1]:
                            while not (nx == play[i][0] and ny == play[i][1]):
                                nx -= dx[k]
                                ny -= dy[k]
                                board[nx][ny] = 1
                    else:
                        break
        # 백돌
        else:
            board[play[i][0]][play[i][1]] = 2
            for k in range(8):
                nx = play[i][0] + dx[k]
                ny = play[i][1] + dy[k]
                while 0 <= nx < n and 0 <= ny < n:
                    # 흑돌이 나왔으면 같은 방향으로 이동한다.
                    if board[nx][ny] == 1:
                        nx += dx[k]
                        ny += dy[k]
                        # 백돌이 나오면 왔던 경로를 되짚어가면서 흑돌을 백돌로(2)로 바꾸어준다.
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 2:
                            # while nx != play[i][0] or ny != play[i][1]:
                            while not (nx == play[i][0] and ny == play[i][1]):
                                nx -= dx[k]
                                ny -= dy[k]
                                board[nx][ny] = 2
                    else:
                        break

    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))
