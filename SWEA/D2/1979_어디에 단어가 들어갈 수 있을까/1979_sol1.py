import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1

    print('#{} {}'.format(tc, ans))
