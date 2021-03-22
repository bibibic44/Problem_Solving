# 함수 사용
# 문제를 처음에 잘못 이해해서 헤맸다.(바보) B의 부분 문자열 중 A에 가장 포함된 문자열을 찾고 있었는데... B를 쪼갤 이유가 전혀 없었다.
# B 전체가 인덱스 중복 없이 A 안에 몇 개가 들어있는 지를 알면 되는 (개)쉬운 문제를 그만... 대쓱 ㅎㅎ
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    def func(b, len_b):
        idx = 0
        cnt = 0
        while idx+len_b <= len(A):
            if A[idx:idx+len_b] == b:
                cnt += 1
                idx += len_b
            else:
                idx += 1

        return len(A) - (cnt*len_b) + cnt


    ans = len(A)
    tmp = func(B, len(B))
    if ans > tmp:
        ans = tmp

    print('#{} {}'.format(tc, ans))
