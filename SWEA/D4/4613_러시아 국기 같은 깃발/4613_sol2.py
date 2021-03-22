import sys
sys.stdin = open('input.txt')


def pick_color(white_line, line):
    global cnt
    if len(line) == 2:
        white = blue = red = 0
        # 하얀색
        for i in range(line[0]):
            for j in range(m):
                if flag[i][j] != 'W':
                    white += 1
        # 파란색
        for i in range(line[0], line[1]):
            for j in range(m):
                if flag[i][j] != 'B':
                    blue += 1
        # 빨간색
        for i in range(line[1], n):
            for j in range(m):
                if flag[i][j] != 'R':
                    red += 1

        if white + blue + red < cnt:
            cnt = white + blue + red

        return

    for i in range(white_line+1, n):
        line.append(i)
        white_line = i
        pick_color(white_line, line)
        line.pop()


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]

    cnt = n*m
    pick_color(0, [])

    print('#{} {}'.format(tc, cnt))



