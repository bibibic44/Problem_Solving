import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    check = [False for _ in range(n)]

    ans = 10000

    def func(col, sum_tmp):
        global ans

        if col == n:
            if sum_tmp < ans:
                ans = sum_tmp
            return
        # 백 트래킹을 하지 않으면 시간초과가 발생한다. O(n^n)이므로 최대 시행 횟수는 9^9, 제한 시간은 2초(대략 4천만번)이므로 Fail
        if ans <= sum_tmp:
            return

        for row in range(n):
            if not check[row]:
                check[row] = True
                func(col+1, sum_tmp+nums[col][row])
                check[row] = False


    func(0, 0)
    print('#{} {}'.format(tc, ans))
