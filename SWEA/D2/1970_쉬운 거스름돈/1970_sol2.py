import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    money = [0 for _ in range(8)]
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(len(money_list)):
        while money_list[i] <= n:
            n -= money_list[i]
            money[i] += 1

    print('#{}\n{}'.format(tc, ' '.join(map(str, money))))

