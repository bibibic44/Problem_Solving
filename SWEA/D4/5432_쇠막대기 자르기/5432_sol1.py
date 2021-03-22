# 스택
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a = input()
    stick = []
    ans = 0

    for i in range(len(a)):
        if a[i] == '(':
            stick.append(i)

        # a[i] = ')'
        else:
            # 레이저
            if i-1 in stick:
                stick.pop()
                ans += len(stick)
            # 막대기의 끝
            else:
                stick.pop()
                # ---|--
                # ---|----|--
                # +2 (+1)+1(+1)
                ans += 1

    print('#{} {}'.format(tc, ans))
