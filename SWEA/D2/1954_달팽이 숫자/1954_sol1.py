import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    a = [[0] * n for _ in range(n)]
    direction = 1
    x = 0
    y = -1
    cnt = 1
    tmp = n
    while tmp > 0:
        for i in range(tmp):
            y += direction
            a[x][y] = cnt
            cnt += 1
        tmp -= 1
        for i in range(tmp):
            x += direction
            a[x][y] = cnt
            cnt += 1
        direction *= -1

    print('#{}'.format(tc))
    for i in range(n):
        print(' '.join(map(str, a[i])))
