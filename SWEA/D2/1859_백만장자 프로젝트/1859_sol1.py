import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    val = list(map(int, input().split()))

    profit = 0
    max_val = val[n-1]

    for i in range(n-2, -1, -1):
        if val[i] < max_val:
            profit += max_val - val[i]
        else:
            max_val = val[i]

    print('#{} {}'.format(tc, profit))
