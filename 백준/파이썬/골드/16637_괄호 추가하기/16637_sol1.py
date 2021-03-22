import copy

ans = -(2 ** 31)


def func(idx, ex, n):
    global ans

    # 선택된 연산자 우선 계산
    if idx == n:
        tmp = copy.deepcopy(ex)
        for i in range(1, n, 2):
            if tmp[i][2]:
                if tmp[i][1] == '+':
                    # 계산하고 첫 번째 항에 값을 저장
                    tmp[i-1][0] += tmp[i+1][0]
                    # 나머지 항은 0, '+' 상태
                    # 나중에 계산하기 편하게 하기 위함
                    tmp[i][1] = '+'
                    tmp[i+1][0] = 0

                elif tmp[i][1] == '-':
                    tmp[i-1][0] -= tmp[i+1][0]
                    tmp[i][1] = '+'
                    tmp[i+1][0] = 0

                elif tmp[i][1] == '*':
                    tmp[i-1][0] *= tmp[i+1][0]
                    tmp[i][1] = '+'
                    tmp[i+1][0] = 0

        val = tmp[0][0]
        for i in range(1, n, 2):
            if tmp[i][1] == '+':
                val += tmp[i+1][0]
            elif tmp[i][1] == '-':
                val -= tmp[i+1][0]
            elif tmp[i][1] == '*':
                val *= tmp[i+1][0]
        # 최고값 갱신
        if ans < val:
            ans = val

        return

    if idx == 1:
        ex[idx][2] = True
        func(idx+2, ex, n)
        ex[idx][2] = False
        func(idx+2, ex, n)

    # 선택할 수 있는 연산자는 연속할 수 없다.
    # 숫자 연산자 숫자 ... 순이므로 연산자끼리는 인덱스가 2씩 차이난다.
    if idx > 1:
        if not ex[idx-2][2]:
            ex[idx][2] = True
            func(idx+2, ex, n)
            ex[idx][2] = False
            func(idx+2, ex, n)
        else:
            func(idx+2, ex, n)


n = int(input())
a = list(input())

# 각 요소는 [숫자, 부호, bool]로 이루어져 있다.
ex = [[0, '+', False] for _ in range(n)]

for i in range(len(a)):
    if '0' <= a[i] <= '9':
        ex[i][0] = int(a[i])
    elif a[i] == '+' or a[i] == '-' or a[i] == '*':
        ex[i][1] = a[i]

# 길이가 1일 경우
if n == 1:
    print(int(a[0]))
# 길이가 1 초과인 경우
else:
    func(1, ex, n)
    print(ans)
