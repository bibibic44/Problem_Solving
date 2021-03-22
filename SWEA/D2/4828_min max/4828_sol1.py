import sys
sys.stdin = open('input.txt')

T = int(input())

def max_value(args):
    ans = -1
    for arg in args:
        if ans == -1 or ans < arg:
            ans = arg
    return ans

def min_value(args):
    ans = -1
    for arg in args:
        if ans == -1 or ans > arg:
            ans = arg
    return ans

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    res = max_value(nums) - min_value(nums)

    print('#{} {}'.format(tc, res))
