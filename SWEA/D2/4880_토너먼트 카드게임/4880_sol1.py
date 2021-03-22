import sys
sys.stdin = open('input.txt')


def divide_gamers(s, e):
    # 1명이 된 경우
    if s == e:
        return s
    mid = (s + e) // 2
    gamer1 = divide_gamers(s, mid)
    gamer2 = divide_gamers(mid + 1, e)
    # 가위바위보
    winner = rock_paper_scissors(gamer1, gamer2)

    return winner


def rock_paper_scissors(gamer1, gamer2):
    # gamer1이 가위
    if cards[gamer1] == 1:
        # gamer1이 승리
        if cards[gamer2] == 1 or cards[gamer2] == 3:
            return gamer1
        # gamer1이 패배
        else:
            return gamer2
    # gamer1이 바위
    elif cards[gamer1] == 2:
        # gamer1이 승리
        if cards[gamer2] == 2 or cards[gamer2] == 1:
            return gamer1
        # gamer1이 패배
        else:
            return gamer2
    # gamer1이 보
    elif cards[gamer1] == 3:
        # gamer1이 승리
        if cards[gamer2] == 3 or cards[gamer2] == 2:
            return gamer1
        # gamer1이 패배
        else:
            return gamer2


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cards = list(map(int, input().split()))

    # 인덱스는 0부터 시작하기 때문에 1을 더해준다.
    ans = divide_gamers(0, n-1) + 1
    print('#{} {}'.format(tc, ans))






