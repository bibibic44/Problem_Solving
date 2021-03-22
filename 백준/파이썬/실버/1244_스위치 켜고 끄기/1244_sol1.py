n = int(input())
switch = list(map(int, input().split()))
m = int(input())
std = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    # 남학생
    if std[i][0] == 1:
        for j in range(n):
            if (j+1) % std[i][1] == 0:
                # 1 0 토글 처리 기법:
                # toggle = 0 or 1 -----> toggle = 1 - toggle
                switch[j] = 1 - switch[j]
    # 여학생
    else:
        switch[std[i][1] - 1] = 1 - switch[std[i][1] - 1]
        for j in range(1, std[i][1]):
            # 왼쪽: std[i][1] - 1 - j, 기준: std[i][1] - 1, 오른쪽: std[i][1] - 1 +j
            if 0 <= std[i][1] - 1 - j and std[i][1] - 1 + j < n and \
                    switch[std[i][1] - 1 - j] == switch[std[i][1] - 1 + j]:
                # 좌우 대칭이면 토글
                switch[std[i][1] - 1 - j] = 1 - switch[std[i][1] - 1 - j]
                switch[std[i][1] - 1 + j] = 1 - switch[std[i][1] - 1 + j]
            # 좌우 대칭인 최대구간만큼 토글해야 하므로 좌우 대칭이 아니면 바로 break 한다.
            # (이 부분을 놓쳐서 틀렸다... 테스트 케이스를 찾아보려고 했는데, 오답은 역시 스스로 고민하는 게 좋다.)
            else:
                break

if n > 20:
    idx = 0
    while idx < n:
        if idx+20 < n:
            print(' '.join(map(str, switch[idx:idx+20])))
            idx += 20
        else:
            print(' '.join(map(str, switch[idx:n])))
            break
else:
    print(' '.join(map(str, switch)))

'''
21
0 1 0 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2
1 3
2 3
1 0 0 0 1 1 0 1 0 1 1 0 1 1 0 1 1 0 1 1
0
'''