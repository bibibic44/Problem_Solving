import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, list(input())))
    counter = [0] * 10
    # 2가 되면 성공
    is_babygin = 0

    for card in cards:
        counter[card] += 1

    for idx in range(len(counter)):
        # triplet 검증
        # 2개의 triplet이 있을 수 있으니 2번 실행
        for double in range(2):
            if counter[idx] >= 3:
                is_babygin += 1
                counter[idx] -= 3
        # run 검증
        # 2개의 run이 있을 수 있으니 2번 실행
        if idx < 8:
            for double in range(2):
                if counter[idx] and counter[idx+1] and counter[idx+2]:
                    is_babygin += 1
                    counter[idx] -= 1
                    counter[idx+1] -= 1
                    counter[idx+2] -= 1
    if is_babygin == 2:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))