import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # eggs[i][0]: 내구도, eggs[i][1]: 무게
    eggs = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    is_check = [False] * n


    def egg_crash(idx, cnt):
        global ans

        if idx == n:
            # 재귀에서 return 안 쓰면 에러난다!
            if ans < cnt:
                ans = cnt
            return

        # 깨진 달걀을 손에 쥐었을 경우
        if is_check[idx]:
            egg_crash(idx+1, cnt)

        else:
            for i in range(n):
                if i == idx or is_check[i]:
                    if i == n-1:
                        egg_crash(idx+1, cnt)
                    continue
                # 달걀로 달걀을 내리친다.
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                # 깨졌을 경우
                if eggs[idx][0] <= 0:
                    is_check[idx] = True
                    cnt += 1
                if eggs[i][0] <= 0:
                    is_check[i] = True
                    cnt += 1

                egg_crash(idx+1, cnt)

                # 원상복구
                if eggs[idx][0] <= 0:
                    is_check[idx] = False
                    cnt -= 1
                if eggs[i][0] <= 0:
                    is_check[i] = False
                    cnt -= 1
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]


    egg_crash(0, 0)
    print(ans)
