# DP: bottom-up
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n //= 10

    memo = [0] * (n+1)
    # bottom-up
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + 2*memo[i-2]

    print('#{} {}'.format(tc, memo[n]))

