import sys
sys.stdin = open('input.txt')

T = int(input())

# 주석 작성
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # # input test
    # print(n, m, a, b)

    ans = 0
    # a의 길이(n)이 b의 길이(m)보다 짧을 때
    if n < m:
        # n의 시작 위치는 m의 인덱스 기준, 0 <= i <= m-n
        for i in range(m-n+1):
            tmp = 0
            for j in range(n):
                # a와 b의 인덱스 접근 시 주의! 둘의 인덱스는 같지 않다.
                tmp += a[j] * b[i+j]
            if ans < tmp:
                ans = tmp
    # a와 b의 길이가 같을 때
    elif n == m:
        for i in range(n):
            ans = a[i] * b[i]
    # b의 길이(m)이 a의 길이(n)보다 짧을 때
    else:
        # m의 시작 위치는 n의 인덱스 기준, 0 <= i <= n-m
        for i in range(n-m+1):
            tmp = 0
            for j in range(m):
                tmp += a[i+j] * b[j]
            if ans < tmp:
                ans = tmp

    print('#{} {}'.format(tc, ans))

