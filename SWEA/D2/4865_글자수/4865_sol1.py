import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    ans = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                cnt += 1
        if ans < cnt:
            ans = cnt

    print('#{} {}'.format(tc, ans))
