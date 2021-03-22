# 카운팅 정렬 구현
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    max_num = 100

    def counting_sort():
        # 각 숫자의 개수 카운트
        cnt = [0] * max_num
        for i in range(n):
            cnt[nums[i]-1] += 1

        # 개수의 누적합 구하기
        cnt_arr = [0] * max_num
        cnt_arr[0] = cnt[0]
        for i in range(1, max_num):
            cnt_arr[i] = cnt_arr[i-1] + cnt[i]

        # 오름차순 정렬
        sorted_arr = [0] * n
        for i in range(n-1, -1, -1):
            sorted_arr[cnt_arr[nums[i]-1]-1] = nums[i]
            cnt_arr[nums[i]-1] -= 1

        return sorted_arr

    sorted_arr = counting_sort()
    ans = []
    for i in range(n):
        ans.append(sorted_arr[n-1-i])
        if i == (n-1)//2:
            if n % 2 == 0:
                ans.append(sorted_arr[i])
            break
        ans.append(sorted_arr[i])
        if len(ans) == 10:
            break

    print('#{} {}'.format(tc, ' '.join(map(str, ans))))
