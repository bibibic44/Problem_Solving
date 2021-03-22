import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    p, a, b = map(int, input().split())


    def find_page(s, e, x):
        if s > e:
            return 0

        middle = (s+e) // 2

        if x == middle:
            return 1

        # 이진탐색 자체에는 문제가 없지만, middle에 +1, -1을 함으로서 검색 횟수가 달라지는 경우가 발생한다!
        elif x > middle:
            # return find_page(middle+1, e, x) + 1 은 오답
            return find_page(middle, e, x) + 1

        else:
            # return find_page(s, middle-1, x) + 1 은 오답
            return find_page(s, middle, x) + 1

    if find_page(1, p, a) > find_page(1, p, b):
        print('#{} B'.format(tc))
    elif find_page(1, p, a) == find_page(1, p, b):
        print('#{} 0'.format(tc))
    else:
        print('#{} A'.format(tc))
