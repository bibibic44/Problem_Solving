import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    exp = list(input())
    for i in range(0, n, 2):
        exp[i] = int(exp[i])

    ans = -(2 ** 31)
    m = n // 2

    for x in range(1 << m):
        check = True
        for i in range(m-1):
            if x & (1 << i) and x & (1 << (i+1)):
                check = False
                break
        if not check:
            continue

        tmp = exp[:]
        # 새로운 식을 담을 리스트 new_exp
        new_exp = []

        # exp를 순회하면서 괄호는 계산해서 담고 일반 연산자와 피연산자는 그냥 담는다.
        # exp 내의 연산자와 피연산자가 동일한 순서대로 담기게 된다.
        for i in range(m):
            idx = 2*i + 1
            # 괄호를 계산한 결과를 new_exp에 담는다. 사용한 피연산자는 -1로 바꾸어 준다. 사용한 연산자는 내버려둔다.
            if x & (1 << i):
                if tmp[idx] == '+':
                    new_exp.append(tmp[idx-1] + tmp[idx+1])
                    tmp[idx-1] = tmp[idx+1] = -1
                elif tmp[idx] == '-':
                    new_exp.append(tmp[idx-1] - tmp[idx+1])
                    tmp[idx-1] = tmp[idx+1] = -1
                elif tmp[idx] == '*':
                    new_exp.append(tmp[idx-1] * tmp[idx+1])
                    tmp[idx-1] = tmp[idx+1] = -1
            # 괄호로 묶이지 않은 연산자를 new_exp에 담는다.
            else:
                # 연산자의 왼쪽 피연산자가 new_exp에 추가되지 않았을 경우 추가한다.
                if tmp[idx-1] != -1:
                    new_exp.append(tmp[idx-1])
                    tmp[idx-1] = -1
                new_exp.append(tmp[idx])

        # 마지막 숫자가 누락되었을 경우 추가
        if tmp[n-1] != -1:
            new_exp.append(tmp[n-1])
        # * 먼저 계산
        i = 1
        # len(new_exp)와 n 혼동 주의!
        while i < len(new_exp):
            if new_exp[i] == '*':
                j = i
                # j < len(new_exp)가 없으면 indexError가 발생한다. and len(new_exp)와 n 혼동 주의!
                # * 이 연속되어 있을 경우 전부 계산한다.
                while j < len(new_exp) and new_exp[j] == '*':
                    new_exp[i-1] *= new_exp[j+1]
                    new_exp[j+1] = 1
                    j += 2
                i = j
            else:
                i += 2
        # +, - 계산
        val = new_exp[0]
        for i in range(1, len(new_exp), 2):
            if new_exp[i] == '+':
                val += new_exp[i+1]
            elif new_exp[i] == '-':
                val -= new_exp[i+1]
            elif new_exp[i] == '*':
                val *= new_exp[i+1]
        if ans < val:
            ans = val

    print(ans)
