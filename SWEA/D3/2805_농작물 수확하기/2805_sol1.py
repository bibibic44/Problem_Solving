import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    mtx = [input() for _ in range(n)]
    ans = 0
    half = n // 2

    # 0번 라인부터 half 라인까지
    for i in range(0, half+1):
        ans += int(mtx[i][half])
        for j in range(1, i+1):
            ans += int(mtx[i][half+j])
            ans += int(mtx[i][half-j])
    # half+1 라인부터 n-1 라인까지
    for i in range(half+1, n):
        ans += int(mtx[i][half])
        for j in range(1, n-i):
            ans += int(mtx[i][half+j])
            ans += int(mtx[i][half-j])

    print('#{} {}'.format(tc, ans))

