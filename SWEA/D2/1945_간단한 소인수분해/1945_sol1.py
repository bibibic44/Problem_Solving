import sys
sys.stdin = open('input.txt')

T = int(input())

def func(num, n):
    if num == 1:
        return 0
    cnt = 0
    if num % n == 0:
        cnt = func(num//n, n) + 1
    else:
        return cnt

    return cnt


for tc in range(1, T+1):
    num = int(input())

    a = func(num, 2)
    b = func(num, 3)
    c = func(num, 5)
    d = func(num, 7)
    e = func(num, 11)

    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))
