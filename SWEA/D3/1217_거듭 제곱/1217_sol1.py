import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_case = int(input())
    n, m = map(int, input().split())

    def exponentiation(n, m, ans):
        if m == 0:
            return ans

        ans = exponentiation(n, m-1, ans*n)
        return ans

    print('#{} {}'.format(tc, exponentiation(n, m, 1)))
