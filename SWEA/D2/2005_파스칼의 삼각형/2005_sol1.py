import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    memo = [[] * n for _ in range(n)]
    memo[0].append(1)
    for i in range(1, n):
        for j in range(i+1):
            if j == 0 or j == i:
                memo[i].append(1)
            else:
                memo[i].append(memo[i-1][j-1] + memo[i-1][j])

    print('#{}'.format(tc))
    for i in range(n):
        print(' '.join(map(str, memo[i])))
