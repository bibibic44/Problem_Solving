import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    # # input test
    # print(T, n, m, nums)

    max_value = -1
    min_value = -1

    for i in range(n-m+1):
        total = 0
        for j in range(i, i+m):
            total += nums[j]
        if max_value == -1 or max_value < total:
            max_value = total
        if min_value == -1 or min_value > total:
            min_value = total

    print('#{} {}'.format(tc, max_value-min_value))
