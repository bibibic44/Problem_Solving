import sys
sys.stdin = open('input.txt')

T = int(input())


def under_station(current, charger):
    ans = -1
    for i in range(len(charger)):
        if charger[i] <= current:
            # 현재 위치보다 같거나 작은 충전 정류장에서 다음 충전 정류장까지의 거리가 k를 초과할 때
            # ---> 현재 위치에서 k 만큼의 차이가 나지만, 충전 정류장에 도달하지는 못한 경우
            if current - charger[i] >= k and current != charger[i]:
                continue
            else:
                ans = charger[i]
        else:
            break
    return ans


for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    charger = list(map(int, input().split()))

    # # input test
    # print(T, k, n, m, charger)

    cnt = 0
    current = 0
    while current <= n:
        # 인덱스가 현재 위치+k 보다 같거나 작은 충전 정류장 중에서 가장 큰 정류장
        station = under_station(current+k, charger)
        if station != -1:
            cnt += 1
            current = station
            # 충전 후 종점 도착 가능한 경우
            if current + k >= n:
                break
        else:
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))
