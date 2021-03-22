import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    good_std = list(map(int, input().split()))

    ans = []
    for i in range(1, n+1):
        if i not in good_std:
            ans.append(i)

    print('#{} {}'.format(tc, ' '.join(map(str, ans))))
