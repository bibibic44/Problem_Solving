import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    orig = input()
    now = '0'
    cnt = 0
    for i in range(len(orig)):
        if now != orig[i]:
            cnt += 1
            now = orig[i]

    print('#{} {}'.format(tc, cnt))
