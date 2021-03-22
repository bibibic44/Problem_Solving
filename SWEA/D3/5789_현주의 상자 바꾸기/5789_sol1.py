import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, q = map(int, input().split())
    boxes = [0] * n

    num = 1
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            boxes[j] = num
        num += 1

    print('#{}'.format(tc), end=' ')
    for i in range(n):
        if i == n-1:
            print(boxes[i])
        else:
            print(boxes[i], end=' ')
