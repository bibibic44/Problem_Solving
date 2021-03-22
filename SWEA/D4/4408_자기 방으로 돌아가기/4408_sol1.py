import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    std = [list(map(int, input().split())) for _ in range(n)]
    # 도착지가 홀수방인 경우, 짝수방으로 바꾸어준다.
    for i in range(n):
        if std[i][1] % 2:
            std[i][1] += 1

    room = [0] * 801
    ans = 0
    for i in range(n):
        if std[i][0] > std[i][1]:
            for p in range(std[i][1], std[i][0] + 1):
                room[p] += 1
                if ans < room[p]:
                    ans = room[p]
        else:
            for p in range(std[i][0], std[i][1] + 1):
                room[p] += 1
                if ans < room[p]:
                    ans = room[p]

    print('#{} {}'.format(tc, ans))
