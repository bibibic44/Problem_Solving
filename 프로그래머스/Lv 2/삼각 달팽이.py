def solution(n):
    answer = []
    tmp = [[0] * n for _ in range(n)]
    direction = 1
    x = -1
    y = 0
    cnt = 1

    l = n
    while n > 0:
        for i in range(n):
            x += direction
            tmp[x][y] = cnt
            cnt += 1
        n -= 1
        for i in range(n):
            y += direction
            tmp[x][y] = cnt
            cnt += 1
        n -= 1
        for i in range(n):
            x -= direction
            y -= direction
            tmp[x][y] = cnt
            cnt += 1
        n -= 1

    for i in range(l):
        for j in range(l):
            if tmp[i][j] != 0:
                answer.append(tmp[i][j])

    return answer