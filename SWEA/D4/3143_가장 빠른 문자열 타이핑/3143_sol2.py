# 함수 사용 X
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    ans = len(A)
    idx = 0
    cnt = 0
    while idx + len(B) <= len(A):
        if A[idx:idx+len(B)] == B:
            cnt += 1
            idx += len(B)
        else:
            idx += 1
    if ans > len(A) - (cnt*len(B)) + cnt:
        ans = len(A) - (cnt*len(B)) + cnt

    print('#{} {}'.format(tc, ans))
