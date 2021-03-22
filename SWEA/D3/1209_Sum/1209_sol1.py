import sys
sys.stdin = open('input.txt')

T = 10


def sum_col_func(a, n, i):
    res = 0
    x = 0
    while 0 <= x < n:
        res += a[x][i]
        x += 1
    return res


def sum_row_func(a, n, i):
    res = 0
    y = 0
    while 0 <= y < n:
        res += a[i][y]
        y += 1
    return res


def sum_dig_func(a, n):
    res1 = 0
    x1 = 0
    y1 = 0
    while 0 <= x1 < n and 0 <= y1 < n:
        res1 += a[x1][y1]
        x1 += 1
        y1 += 1

    res2 = 0
    x2 = 0
    y2 = n-1
    while 0 <= x2 < n and 0 <= y2 < n:
        res2 += a[x2][y2]
        x2 += 1
        y2 -= 1

    res = res1 if res1 >= res2 else res2

    return res


for tc in range(1, T+1):
    n = 100
    tc_num = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    sum_dig = sum_dig_func(a, n)
    for i in range(n):
        sum_col = sum_col_func(a, n, i)
        sum_row = sum_row_func(a, n, i)
        if ans < sum_col:
            ans = sum_col
        if ans < sum_row:
            ans = sum_row
        if ans < sum_dig:
            ans = sum_dig

    print('#{} {}'.format(tc, ans))

