import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    test_case, n = input().split()
    n = int(n)
    input_str = list(input().split())

    nums = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    tmp = [[] for _ in range(10)]

    # 0 ~ 9에 해당하는 글자를 tmp의 순서에 맞게 삽입
    for i in range(n):
        tmp[nums[input_str[i]]] += [input_str[i]]

    print('#{}'.format(tc))
    for i in range(10):
        # tmp = [['ZRO'], ['ONE'], ..., ['NIN']]
        if tmp[i]:
            print(' '.join(tmp[i]), end=' ')
    # 개행
    print()
