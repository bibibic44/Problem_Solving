import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    test_case, n = input().split()
    n = int(n)
    input_str = list(input().split())

    nums = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    num_keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    tmp = [0] * 10

    # 개수를 카운트 하여 카운트 수만큼 num_keys의 값을 출력
    for i in range(n):
        tmp[nums[input_str[i]]] += 1

    print('#{}'.format(tc))
    for i in range(10):
        # tmp[i] = 0 ~ 9까지 숫자들의 개수
        for j in range(tmp[i]):
            if i == 9 and j == tmp[i]-1:
                print(num_keys[i])
            else:
                print(num_keys[i], end=' ')
