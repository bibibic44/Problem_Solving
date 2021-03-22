import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num, cnt = map(int, input().split())
    num = list(map(int, list(str(num))))
    is_max = False

    for i in range(len(num)):
        for j in range(len(num)-1, i, -1):
            if cnt == 0:
                break
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]
                cnt -= 1

    res = 0
    if cnt != 0:
        if cnt % 2 == 0:
            for i in range(len(num)):
                res += num[i] * (10 ** (len(num)-1-i))
        else:
            num[len(num)-2], num[len(num)-1] = num[len(num)-1], num[len(num)-2]
            for i in range(len(num)):
                res += num[i] * (10 ** (len(num)-1-i))
    else:
        for i in range(len(num)):
            res += num[i] * (10 ** (len(num)-1-i))

    print('#{} {}'.format(tc, res))