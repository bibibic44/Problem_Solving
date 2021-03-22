import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(m):
        tmp = nums.pop(0)
        nums.append(tmp)

    print('#{} {}'.format(tc, nums.pop(0)))
