import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 이렇게 하면 a와 b에 원하는 값이 들어가지 않는다.(한 라인씩 입력된다.)
    # a, b = [list(map(int, input().split())) for _ in range(n)]
    a = []
    b = []
    for _ in range(n):
        tmp1, tmp2 = map(int, input().split())
        a += [tmp1]
        b += [tmp2]
    p = int(input())
    c = [int(input()) for _ in range(p)]

    route = [0] * p
    for i in range(p):
        for j in range(n):
            if a[j] <= c[i] <= b[j]:
                route[i] += 1

    print('#{} {}'.format(tc, ' '.join(map(str, route))))

