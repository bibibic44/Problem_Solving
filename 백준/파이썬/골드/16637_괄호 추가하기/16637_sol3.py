# 비트마스크 + 새로운 리스트에 새로운 식 추가
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    exp = list(input())
    for i in range(0, n, 2):
        exp[i] = int(exp[i])

    ans = -(2 ** 31)
    m = n // 2

    for x in range(1 << m):
        check = True
        for i in range(m-1):
            if x & (1 << i) and x & (1 << (i+1)):
                check = False
                break
        if not check:
            continue

        tmp = exp[:]
        new_exp = []

        for i in range(m):
            idx = 2*i + 1
            if x & (1 << i):
                if tmp[idx] == '+':
                    new_exp.append(tmp[idx-1] + tmp[idx+1])
                    tmp[idx-1] = tmp[idx+1] = -1
                elif tmp[idx] == '-':
                    new_exp.append(tmp[idx-1] - tmp[idx+1])
                    tmp[idx-1] = tmp[idx+1] = -1
                elif tmp[idx] == '*':
                    new_exp.append(tmp[idx-1] * tmp[idx+1])
                    tmp[idx-1] = tmp[idx+1] = -1
            else:
                if tmp[idx-1] != -1:
                    new_exp.append(tmp[idx-1])
                    tmp[idx-1] = -1
                new_exp.append(tmp[idx])

        if tmp[n-1] != -1:
            new_exp.append(tmp[n-1])

        val = new_exp[0]
        for i in range(1, len(new_exp), 2):
            if new_exp[i] == '+':
                val += new_exp[i+1]
            elif new_exp[i] == '-':
                val -= new_exp[i+1]
            elif new_exp[i] == '*':
                val *= new_exp[i+1]
        if ans < val:
            ans = val

    print(ans)