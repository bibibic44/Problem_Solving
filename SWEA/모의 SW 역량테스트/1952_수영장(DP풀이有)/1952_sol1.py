import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range (1, T+1):
    charge = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    def calc(value, month):
        if month >= 13:
            return value

        # ans의 디폴트 값은 연간 이용권
        ans = charge[3]

        # 답이 될 수 없으면 바로 리턴
        if value >= ans:
            return value

        # 일일 이용권
        tmp1 = calc(value + plan[month-1] * charge[0], month+1)
        # 월별 이용권
        tmp2 = calc(value + charge[1], month + 1)
        # 3개월 이용권
        tmp3 = calc(value + charge[2], month + 3)

        ans = min(ans, tmp1, tmp2, tmp3)

        return ans

    print('#{} {}'.format(tc, calc(0, 1)))
