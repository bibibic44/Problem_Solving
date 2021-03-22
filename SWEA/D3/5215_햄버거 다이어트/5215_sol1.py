import sys
sys.stdin = open('input.txt')


def hamburger_score(idx, calories, taste):
    global ans

    if calories > L:
        return

    if idx >= N:
        if ans < taste:
            ans = taste
        return

    hamburger_score(idx+1, calories+hamburger[idx][1], taste+hamburger[idx][0])
    hamburger_score(idx+1, calories, taste)


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    hamburger = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    hamburger_score(0, 0, 0)

    print('#{} {}'.format(tc, ans))
