# 비트마스크

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    a = list(input())

    for i in range(0, n, 2):
        a[i] = int(a[i])

    ans = -(2 ** 31)
    m = n // 2

    for x in range(1 << m):
        check = True
        for i in range(m-1):
            if x & (1 << i) and x & (1 << (i + 1)):
                check = False

        if not check:
            continue

        tmp = a[:]
        for i in range(m):
            if x & (1 << i):
                k = 2*i + 1
                if tmp[k] == '+':
                    tmp[k-1] += tmp[k+1]
                    tmp[k] = '+'
                    tmp[k+1] = 0
                elif tmp[k] == '-':
                    tmp[k-1] -= tmp[k+1]
                    tmp[k] = '+'
                    tmp[k+1] = 0
                elif tmp[k] == '*':
                    tmp[k-1] *= tmp[k+1]
                    tmp[k] = '+'
                    tmp[k+1] = 0
        val = tmp[0]
        for i in range(1, n, 2):
            if tmp[i] == '+':
                val += tmp[i+1]
            elif tmp[i] == '-':
                val -= tmp[i+1]
            elif tmp[i] == '*':
                val *= tmp[i+1]

        if ans < val:
            ans = val

    print(ans)
