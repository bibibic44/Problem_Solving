import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a = input()
    stick = 0
    ans = 0

    for i in range(len(a)):
        if a[i] == '(':
            stick += 1
        # a[i] = ')'
        else:
            # 레이저
            if a[i-1] == '(':
                stick -= 1
                ans += stick
            # 막대기의 끝
            else:
                stick -= 1
                # ---|--
                # ---|----|--
                # +2 (+1)+1(+1)
                ans += 1

    print('#{} {}'.format(tc, ans))
