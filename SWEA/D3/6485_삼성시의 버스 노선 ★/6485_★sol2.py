# 딕셔너리 이용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # dic[5000] 을 0으로 초기화
    d = {i: 0 for i in range(5000)}

    for i in range(n):
        # 시작점, 끝점 입력
        s, e = map(int, input().split())
        # 해당 범위에 속하면 값을 1씩 더해준다.
        # 딕셔너리의 인덱스는 0에서부터 시작하기 때문에 -1을 해준다.
        for j in range(s-1, e):
            d[j] += 1

    res = []
    p = int(input())
    for i in range(p):
        # 정류장 인덱스를 입력받아 키로 삼는다. 노선의 개수를 res에 저장한다.
        # 마찬가지로 딕셔너리의 인덱스가 0부터 시작하기 때문에 정류장의 인덱스도 -1을 해준다.
        res += [d[int(input())-1]]

    print('#{} {}'.format(tc, ' '.join(map(str, res))))
