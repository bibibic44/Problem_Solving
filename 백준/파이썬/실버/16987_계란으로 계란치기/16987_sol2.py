# 백준 코드 참고
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # eggs[i][0]: 내구도, eggs[i][1]: 무게
    eggs = [list(map(int, input().split())) for _ in range(n)]


    def egg_crash(idx):
        if idx == n:
            cnt = 0
            for i in range(n):
                if eggs[i][0] <= 0:
                    cnt += 1
            return cnt

        # 깨진 달걀을 손에 쥐었을 경우
        if eggs[idx][0] <= 0:
            return egg_crash(idx+1)

        ans = 0
        crashed = False
        for i in range(n):
            # 자기 자신은 내리칠 수 없다.
            if i == idx:
                continue
            # 내리칠 달걀이 깨지지 않은 경우에만 내리친다.
            if eggs[i][0] > 0:
                # 손에 쥔 달걀로 내리치는 상황 ---> crashed = True
                # 마지막 달걀로 내리칠 수 있는 상황일 때(깨지지 않은 달걀이 있을 때) 대비
                crashed = True
                # 달걀로 달걀을 내리친다.
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]

                tmp = egg_crash(idx+1)

                if ans < tmp:
                    ans = tmp

                # 원상복구
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]

        # 손에 쥔 달걀로 내리치지 못한 상황 ---> crashed = False
        # 마지막 달걀로 내리칠 수 없는 상황일 때(마지막 달걀을 제외한 모든 달걀이 깨져 있을 때)
        if not crashed:
            return egg_crash(idx + 1)

        return ans


    print(egg_crash(0))
