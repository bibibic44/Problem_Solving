import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, k = map(int, input().split())
    ans = 0
    for i in range(1 << 12):
        bit_sum = 0
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                bit_sum += a[j]
                if cnt > n:
                    break
        if bit_sum == k and cnt == n:
            ans += 1

    print('#{} {}'.format(tc, ans))
