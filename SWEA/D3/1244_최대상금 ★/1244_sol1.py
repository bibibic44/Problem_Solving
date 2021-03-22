import sys
sys.stdin = open('input.txt')

T = int(input())

# 내림차순일 경우 돌아가지 않는다...
def func(num, idx, cnt, n):
    if cnt == n:
        return int(''.join(num))
    l = len(num)
    ans = 0
    for i in range(idx, l-1):
        for j in range(i+1, l):
            # 이 if 문이 없으면 시간 초과!
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]
                tmp = func(num, i, cnt+1, n)
                if ans < tmp:
                    ans = tmp
                num[i], num[j] = num[j], num[i]
                # 111111 10 같은 경우 여전히 시간 초과가 뜬다.
                # 111119 10, 191319 10 같은 경우까지 고려 ---> 단순 스왑 X, n을 함부로 건드리는 것도 X
            elif num[i] == num[j]:
                continue
    return ans

for tc in range(1, T+1):
    num, n = map(int, input().split())
    num = list(str(num))

    # func는 swap하면서 최대값을 리턴하는 함수
    ans = func(num, 0, 0, n)

    # func에서 중복된 값 때문에 교환이 되지 않은 경우 or 내림차순이라 교환이 되지 않은 경우
    if ans == 0:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                if n == 0:
                    break
                # 중복일 경우
                if num[i] <= num[j]:
                    num[i], num[j] = num[j], num[i]
                    n -= 1
        # 내림차순일 경우
        if num == sorted(num, reverse=True):
            # n이 짝수면 그대로 출력해도 되지만, 홀수면 맨 뒤의 값 2개를 swap 해준다.
            if n % 2:
                num[len(num)-1], num[len(num)-2] = num[len(num)-2], num[len(num)-1]
        ans = int(''.join(num))

    print('#{} {}'.format(tc, ans))