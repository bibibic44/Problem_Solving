# 위에서부터 시작
import sys
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T+1):
    n = 100
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(n)]

    ans = -1
    for i in range(n):
        if ans != -1:
            break
        if ladder[0][i] == 1:
            nx = 1
            ny = i
            r = False
            l = False
            while nx < n:
                if 0 <= ny+1 < n and ladder[nx][ny+1] == 1 and not l:
                    ny += 1
                    r = True
                elif 0 <= ny-1 < n and ladder[nx][ny-1] == 1 and not r:
                    ny -= 1
                    l = True
                else:
                    nx += 1
                    r = False
                    l = False

                if 0 <= nx < n and ladder[nx][ny] == 2:
                    ans = i
                    break

    print('#{} {}'.format(tc, ans))
