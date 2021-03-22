import sys
sys.stdin = open('input.txt')

T = int(input())

def max_value(cnt):
    card, count = 0, 0
    for i in range(10):
        if count <= cnt[i]:
            count = cnt[i]
            card = i

    return card, count

for tc in range(1, T+1):
    n = int(input())
    cards = list(map(int, list(input())))
    cnt = [0] * 10

    # # input test
    # print(T, n, cards)

    # 카드의 개수 카운트
    for card in cards:
        cnt[card] += 1

    ans = max_value(cnt)

    print('#{} {} {}'.format(tc, ans[0], ans[1]))
