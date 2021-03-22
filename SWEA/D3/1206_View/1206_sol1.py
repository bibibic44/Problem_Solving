import sys
sys.stdin = open('input.txt')

T = 10

def min_value(a, b, c, d):
    tmp1 = a if a <= b else b
    tmp2 = c if c <= d else d
    res = tmp1 if tmp1 <= tmp2 else tmp2

    return res

for tc in range(1, T+1):
    n = int(input())
    b = list(map(int, input().split()))
    res = 0

    for i in range(2, n-2):
        if b[i]-b[i-1] > 0 and b[i]-b[i-2] > 0 and b[i]-b[i+1] > 0 and b[i]-b[i+2] > 0:
            res += min_value(b[i]-b[i-1], b[i]-b[i-2], b[i]-b[i+1], b[i]-b[i+2])

    print('#{} {}'.format(tc, res))
