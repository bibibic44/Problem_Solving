import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]

    # 가장 높은 봉우리의 높이를 구한다.
    highest = 0
    for i in range(N):
        for j in range(N):
            if highest < MAP[i][j]:
                highest = MAP[i][j]

    # 가장 높은 봉우리의 위치를 구한다.
    start = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == highest:
                start.append([i, j])

    # dfs로 가장 긴 등산로를 구하는 함수
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def dfs(x, y, chance, now):
        cnt = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                # 중복 방문 불가
                if not visited[nx][ny]:
                    # 봉우리를 깎지 않고도 방문 가능
                    if now > MAP[nx][ny]:
                        # 방문 표시
                        visited[nx][ny] = True
                        # now = MAP[nx][ny]
                        # chance는 변동 없으므로 넘겨받은 인자를 그대로 써준다. (False로 인자 대입 X! True일지, False일지 모름. )
                        tmp = dfs(nx, ny, chance, MAP[nx][ny]) + 1
                        # cnt에 최댓값 갱신
                        if tmp > cnt:
                            cnt = tmp

                    # 봉우리를 깎아야 방문 가능
                    else:
                        # 깎을 수 있는 기회 보유 and 깎을 수 있는 높이가 충분해야 한다.
                        if not chance and MAP[nx][ny]-now+1 <= K:
                            # chance = True, now = MAP[x][y] - 1
                            # 재귀함수에서 분기별로 변하는 변수는 변수에 대입하지 말고 함수에 인자로 바로 넣는다. (오답노트)
                            # EX) chance = True ---> dfs(chance) X ---> dfs(True)
                            # 만약 변수에 그대로 대입해버리면 재귀함수가 리턴한 뒤에도 해당 변수값이 유지되어 분기를 나눈 의미가 없어진다.
                            tmp = dfs(nx, ny, True, MAP[x][y] - 1) + 1
                            # cnt에 최댓값 갱신
                            if tmp > cnt:
                                cnt = tmp

        visited[x][y] = False
        return cnt


    ans = 0
    for s in start:
        # 시작점도 방문 표시를 해야 한다. (오답노트)
        visited[s[0]][s[1]] = True
        tmp = dfs(s[0], s[1], False, highest)
        visited[s[0]][s[1]] = False
        if ans < tmp:
            ans = tmp
    print('#{} {}'.format(tc, ans))
