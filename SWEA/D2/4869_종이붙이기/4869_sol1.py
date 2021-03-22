# DP: top-down
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n //= 10

    memo = [0] * (n+1)
    # top-down
    def func(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if memo[n] > 0:
            return memo[n]

        memo[n] = func(n-1) + 2*func(n-2)

        return memo[n]

    print('#{} {}'.format(tc, func(n)))

