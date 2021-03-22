import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    block = list(map(int, input().split()))
    ans = 0

    for i in range(len(block)):
        tmp = 0
        for j in range(i+1, len(block)):
            if block[i] > block[j]:
                tmp += 1
        if ans < tmp:
            ans = tmp

    print('#{} {}'.format(tc, ans))