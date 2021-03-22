import sys
sys.stdin = open('input.txt')

while True:
    try:
        tc = int(input())
        nums = list(map(int, input().split()))
    except:
        break

    num = 1
    while nums[-1] != 0:
        if num > 5:
            num = 1
        tmp = nums.pop(0)
        tmp -= num
        num += 1
        if tmp < 0:
            tmp = 0
        nums.append(tmp)

    print('#{} {}'.format(tc, ' '.join(map(str, nums))))
