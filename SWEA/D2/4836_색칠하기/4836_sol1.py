import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    color = [list(map(int, input().split())) for _ in range(n)]
    grid = [[0] * 10 for _ in range(10)]

    cnt = 0
    for x in range(n):
        for i in range(color[x][0], color[x][2]+1):
            for j in range(color[x][1], color[x][3]+1):
                if grid[i][j] == 0:
                    grid[i][j] = color[x][4]
                else:
                    if grid[i][j] != color[x][4]:
                        cnt += 1

    print('#{} {}'.format(tc, cnt))