import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for x in range(n-m+1):
        for y in range(n-m+1):
            cnt = 0
            for i in range(m):
                for j in range(m):
                    cnt += a[x+i][y+j]
            if ans < cnt:
                ans = cnt

    print('#{} {}'.format(tc, ans))
