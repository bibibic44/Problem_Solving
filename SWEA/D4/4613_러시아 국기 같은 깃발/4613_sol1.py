import sys
sys.stdin = open('input.txt')


def color_cnt(color, s, e):
    res = 0
    for i in range(s, e):
        for j in range(m):
            if flag[i][j] != color:
                res += 1
    return res


def calc(line):
    # 하얀색
    white = color_cnt('W', 0, line[0])
    # 파란색
    blue = color_cnt('B', line[0], line[1])
    # 빨간색
    red = color_cnt('R', line[1], n)

    return white + red + blue


def pick_color(white_line, line):
    global cnt
    if len(line) == 2:
        tmp = calc(line)
        if tmp < cnt:
            cnt = tmp
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



