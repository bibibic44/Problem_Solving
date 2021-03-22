n = int(input())
num = int(input())

a = [[0]*n for _ in range(n)]
x, y = n//2, n//2

a[x][y] = 1
cnt = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 홀수 테두리는 2씩 증가한다.
for i in range(1, n+1, 2):
    # dx, dy를 쓰기 위한 k
    for k in range(4):
        # 한 변 당, i-1칸씩 이동한다. 예) 3 -> 2칸씩(_ㅁㅁ), 5 --> 4칸씩(_ㅁㅁㅁㅁ)
        # _ 는 왼쪽 하단에서 왼쪽 상단으로 올라오는 라인에 속한다.
        for j in range(i-1):
            # 한꺼풀이 끝났으면 x를 한 칸 위로 올린다.
            # ㅇXㅇㅇㅇ 여기 X로 올린다.
            # ㅇxㅁㅁㅇ 여기 x를
            if k == 0 and j == 0:
                x -= 1
                cnt += 1
            else:
                x += dx[k]
                y += dy[k]
                cnt += 1

            a[x][y] = cnt

p = []
for i in range(n):
    print(' '.join(map(str, a[i])))
    for j in range(n):
        if a[i][j] == num:
            p.append(i+1)
            p.append(j+1)

print(' '.join(map(str, p)))

