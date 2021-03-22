# DP 사용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range (1, T+1):
    charge = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    memo = [-1]*12

    def calc(month):
        if month <= 0:
            return 0

        if memo[month-1] != -1:
            return memo[month-1]

        # DP를 쓸 때는 점화식 필수! 어떻게 푸는 지 감이 안 잡히는 이유는 점화식을 안 세웠기 때문이다...
        memo[month-1] = min(calc(month-1) + plan[month-1]*charge[0],
                            calc(month-1) + charge[1],
                            calc(month-3) + charge[2],
                            charge[3])
        return memo[month-1]


    print('#{} {}'.format(tc, calc(12)))

