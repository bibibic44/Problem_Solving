import sys
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T+1):
    n = 100
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(n)]

    ans = -1
    ans_cnt = -1
    for i in range(n):
        if ladder[0][i] == 1:
            nx = 1
            ny = i
            r = False
            l = False
            cnt = 0
            while nx < n:
                if 0 <= ny+1 < n and ladder[nx][ny+1] == 1 and not l:
                    ny += 1
                    r = True
                    cnt += 1
                elif 0 <= ny-1 < n and ladder[nx][ny-1] == 1 and not r:
                    ny -= 1
                    l = True
                    cnt += 1
                else:
                    nx += 1
                    r = False
                    l = False
                    cnt += 1

            if ans == -1 or ans_cnt >= cnt:
                ans = i
                ans_cnt = cnt

    print('#{} {}'.format(tc, ans))
