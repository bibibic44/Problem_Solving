# 무한급수 ---> X(이제 못 풀어...)
# 파리가 살아있는 시간(A, B가 충돌하기 전까지의 시간) * 파리의 속력
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    ans = (D / (A+B)) * F
    print('#{} {}'.format(tc, ans))
