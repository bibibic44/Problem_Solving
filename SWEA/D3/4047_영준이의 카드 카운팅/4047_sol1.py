import sys
sys.stdin = open('input.txt')

T = int(input())


def func(input_str):
    spade = [0] * 13
    diamond = [0] * 13
    heart = [0] * 13
    clover = [0] * 13

    input_str_length = len(input_str)
    for i in range(0, input_str_length, 3):
        if input_str[i] == 'S':
            num = int(input_str[i+1:i+3])
            if spade[num-1] == 0:
                spade[num-1] += 1
            else:
                return 'ERROR'
        elif input_str[i] == 'D':
            num = int(input_str[i+1:i+3])
            if diamond[num-1] == 0:
                diamond[num-1] += 1
            else:
                return 'ERROR'
        elif input_str[i] == 'H':
            num = int(input_str[i+1:i+3])
            if heart[num-1] == 0:
                heart[num-1] += 1
            else:
                return 'ERROR'
        elif input_str[i] == 'C':
            num = int(input_str[i+1:i+3])
            if clover[num-1] == 0:
                clover[num-1] += 1
            else:
                return 'ERROR'

    cnt = [0] * 4
    for i in range(13):
        if spade[i] == 0:
            cnt[0] += 1
        if diamond[i] == 0:
            cnt[1] += 1
        if heart[i] == 0:
            cnt[2] += 1
        if clover[i] == 0:
            cnt[3] += 1

    return ' '.join(map(str, cnt))


for tc in range(1, T+1):
    input_str = input()
    print('#{} {}'.format(tc, func(input_str)))
