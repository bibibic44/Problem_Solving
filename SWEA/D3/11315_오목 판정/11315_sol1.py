import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    a = [input() for _ in range(n)]

    def is_check():
        # 가로
        for i in range(n):
            if 'ooooo' in a[i]:
                return 'YES'

        # 세로
        reverse_a = list(map(list, zip(*a)))
        for i in range(n):
            if 'ooooo' in ''.join(reverse_a[i]):
                return 'YES'

        # 대각선 \
        for i in range(n):
            for j in range(n):
                if i+5 <= n and j+5 <= n:
                    for k in range(5):
                        if a[i+k][j+k] != 'o':
                            break
                    else:
                        return 'YES'

        # 대각선 /
        for i in range(n):
            for j in range(n-1, 0, -1):
                if i+5 <= n and j >= 4:
                    for k in range(5):
                        if a[i+k][j-k] != 'o':
                            break
                    else:
                        return 'YES'
        # 없음
        return 'NO'

    print('#{} {}'.format(tc, is_check()))


