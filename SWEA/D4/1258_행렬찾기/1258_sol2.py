import sys
sys.stdin = open('input.txt')


def find_square(x, y, visited):
    row_size = col_size = 0

    # 행의 길이
    for i in range(x, n):
        if mtx[i][y] != 0:
            col_size += 1
        else:
            break

    # 열의 길이
    for i in range(y, n):
        if mtx[x][i] != 0:
            row_size += 1
        else:
            break

    # 방문
    if row_size != 0 and col_size != 0:
        for i in range(x, x+col_size):
            for j in range(y, y+row_size):
                visited[i][j] = True

    # 사각형 크기, 행의 길이, 열의 길이
    return col_size*row_size, col_size, row_size


def ans_print(ans):
    res = [str(len(ans))]
    for i in range(len(ans)):
        res.append(ans[i][1])
        res.append(ans[i][2])

    return ' '.join(map(str, res))


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    mtx = [list(map(int, input().split())) for _ in range(n)]

    ans = []
    visited = [[False for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and mtx[i][j] != 0:
                tmp = find_square(i, j, visited)
                if tmp[0] != 0:
                    ans.append(tmp)
    ans.sort()
    print('#{} {}'.format(tc, ans_print(ans)))
    # print(ans)
    # print(ans_print(ans))