import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_case = int(input())
    n, m = map(int, input().split())

    ans = 1
    def exponentiation(n, m):
        global ans
        if m == 0:
            return
        ans *= n
        exponentiation(n, m-1)
        return


    exponentiation(n, m)
    print('#{} {}'.format(tc, ans))
