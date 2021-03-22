import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    nums = list(map(int, input().split()))
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    if total == 0:
        print('#{} {}'.format(tc+1, 0))
    else:
        print('#{} {}'.format(tc+1, round(total / len(nums))))

