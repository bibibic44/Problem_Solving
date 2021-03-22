import sys
sys.stdin = open('input.txt')

T = int(input())


def Bubble_sort(n, nums):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    Bubble_sort(n, nums)

    # print('#{}'.format(tc), end=' ')
    # for i in range(n):
    #     if i == n-1:
    #         print(nums[i])
    #     else:
    #         print(nums[i], end=' ')

    # 문자열로 출력하기
    # 주의! join은 리스트 안의 값이 '문자열'이어야 한다!
    print('#{} {}'.format(tc, ' '.join(map(str, nums))))

