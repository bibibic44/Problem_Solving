import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    money = [0 for _ in range(8)]

    if 50000 <= n:
        n -= 50000
        money[0] += 1
    elif 10000 <= n:
        n -= 10000
        money[1] += 1
    elif 5000 <= n:
        n -= 5000
        money[2] += 1
    elif 1000 <= n:
        n -= 1000
        money[3] += 1
    elif 500 <= n:
        n -= 500
        money[4] += 1
    elif 100 <= n:
        n -= 100
        money[5] += 1
    elif 50 <= n:
        n -= 50
        money[6] += 1
    elif 10 <= n:
        n -= 10
        money[7] += 1

print('#{}\n{}'.format(tc, ' '.join(map(str, money))))

