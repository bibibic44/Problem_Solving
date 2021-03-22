import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # a = []
    # b = []
    # for _ in range(n):
    #     tmp1, tmp2 = map(int, input().split())
    #     a += [tmp1]
    #     b += [tmp2]
    a = [0] * 5000
    b = [0] * 5000
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    p = int(input())
    c = [int(input()) for _ in range(p)]

    print(a)
    print(b)
    print(c)

