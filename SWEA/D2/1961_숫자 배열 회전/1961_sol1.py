import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [input().split() for _ in range(n)]
    ans = [['']*n for _ in range(n)]

    def rot_right_angle(matrix):
        m = [['']*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] = matrix[n-1-j][i]

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


    # print(list(map(list, zip(*matrix))))

