import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    card = list(input().split())
    ans = []
    half = 0

    if n % 2 == 0:
        half = n//2
    else:
        half = n//2 + 1

    for i in range(half):
        ans.append(card[i])
        if i+half < n:
            ans.append(card[i+half])

    print('#{} {}'.format(tc, ' '.join(ans)))
