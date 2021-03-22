import sys
sys.stdin = open('input.txt')

T = 10

def max_min_find(boxes):
    max_res, min_res = -1, -1
    max_idx, min_idx = 0, 0
    for i in range(len(boxes)):
        if max_res == -1 or boxes[i] > max_res:
            max_res = boxes[i]
            max_idx = i
        if min_res == -1 or boxes[i] < min_res:
            min_res = boxes[i]
            min_idx = i

    return max_idx, min_idx


for tc in range(1, T+1):
    n = int(input())
    boxes = list(map(int, input().split()))

    # # input test
    # print(T, n, box_height)

    ans = 0

    while n > 0:
        max_idx, min_idx = max_min_find(boxes)

        if boxes[max_idx] == boxes[min_idx]:
            if n % 2:
                ans = 2
                break
            else:
                ans = 0
                break
        else:
            boxes[max_idx] -= 1
            boxes[min_idx] += 1

        n -= 1

    max_idx, min_idx = max_min_find(boxes)
    ans = boxes[max_idx] - boxes[min_idx]



    print('#{} {}'.format(tc, ans))


