# zip 함수를 사용해서 로테이션
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [input().split() for _ in range(n)]
    ans = [['']*n for _ in range(n)]

    def rot_right_angle(matrix):
        m = list(map(list, zip(*matrix)))
        for i in range(n):
            m[i].reverse()

        return m

    for x in range(3):
        matrix = rot_right_angle(matrix)
        for i in range(n):
            tmp = ''
            for j in range(n):
                tmp += matrix[i][j]
            ans[i][x] = tmp

    print('#{}'.format(tc))
    for i in range(n):
        print(' '.join(ans[i]))



