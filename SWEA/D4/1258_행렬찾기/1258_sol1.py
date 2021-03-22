import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def find_square(x, y, visited, idx):
    q = []
    q.append([x, y])
    visited[x][y] = idx
    # 연속되어 있는 숫자들 체크
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if mtx[nx][ny] != 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = idx
                    q.append([nx, ny])

    # 사각형 찾기: 행마다 열의 개수를 세어서 row에 저장
    row = []
    for i in range(n):
        tmp = 0
        for j in range(n):
            if visited[i][j] == idx:
                tmp += 1
        if tmp != 0:
            row.append(tmp)

    # 사각형 검출: 정사각형은 False, 열의 개수가 서로 다르면 False
    for i in range(1, len(row)):
        if row[i] == len(row):
            return False, 0, 0, 0
        # 열이 하나가 아니고 행이 하나이면 True
        if len(row) == 1:
            continue
        if row[i] != row[i-1]:
            return False, 0, 0, 0

    # 사각형 여부, 사각형 크기, 행, 열
    return True, row[0]*len(row), len(row), row[0]


def ans_print(ans):
    res = [str(len(ans))]
    for i in range(len(ans)):
        res.append(ans[i][2])
        res.append(ans[i][3])

    return ' '.join(map(str, res))


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    mtx = [list(map(int, input().split())) for _ in range(n)]

    idx = 1
    ans = []
    visited = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and mtx[i][j] != 0:
                tmp = find_square(i, j, visited, idx )
                idx += 1
                if tmp[0]:
                    ans.append(tmp)

    ans.sort()
    print('#{} {}'.format(tc, ans_print(ans)))
    # print(ans)
    # print(ans_print(ans))