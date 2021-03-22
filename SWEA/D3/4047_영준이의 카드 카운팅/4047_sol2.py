import sys
sys.stdin = open('input.txt')

T = int(input())


def func(input_str):
    card = [[0] * 13 for _ in range(4)]

    input_str_length = len(input_str)
    for i in range(0, input_str_length, 3):
        if input_str[i] == 'S':
            num = int(input_str[i+1:i+3])
            if card[0][num-1] == 0:
                card[0][num-1] += 1
            else:
                return 'ERROR'
        elif input_str[i] == 'D':
            num = int(input_str[i+1:i+3])
            if card[1][num-1] == 0:
                card[1][num-1] += 1
            else:
                return 'ERROR'
        elif input_str[i] == 'H':
            num = int(input_str[i+1:i+3])
            if card[2][num-1] == 0:
                card[2][num-1] += 1
            else:
                return 'ERROR'
        elif input_str[i] == 'C':
            num = int(input_str[i+1:i+3])
            if card[3][num-1] == 0:
                card[3][num-1] += 1
            else:
                return 'ERROR'

    cnt = [0] * 4
    for i in range(4):
        for j in range(13):
            if card[i][j] == 0:
                cnt[i] += 1

    return ' '.join(map(str, cnt))


for tc in range(1, T+1):
    input_str = input()
    print('#{} {}'.format(tc, func(input_str)))
