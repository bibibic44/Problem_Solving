# 도착점에서부터 출발
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
        if ladder[n-1][i] == 2:
            nx = n-2
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
                    nx -= 1
                    r = False
                    l = False

                if nx == 0 and ladder[nx][ny] == 1:
                    ans = ny
                    break

    print('#{} {}'.format(tc, ans))
