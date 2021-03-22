# 중위표기식 ---> 후위표기식 ---> 후위표기식 계산
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    n = int(input())
    input_str = input()

    # 중위 표기식 -> 후위 표기식
    s = []
    post = ''
    op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2}
    for c in input_str:
        # c가 피연산자인 경우
        if '0' <= c <= '9':
            post += c
        # c가 연산자인 경우
        else:
            if not s:
                s.append(c)
            else:
                # 연산자의 우선순위를 비교한다.
                # 스택의 top의 우선순위 >= c의 우선순위 ---> top을 pop()한다.
                if c == ')':
                    while s[-1] != '(':
                        post += s.pop()
                    s.pop()
                elif s[-1] != '(' and op_priority[s[-1]] >= op_priority[c]:
                    post += s.pop()
                if c != ')':
                    s.append(c)
    while s:
        post += s.pop()

    # 후위표기식 계산
    for c in post:
        # c가 피연산자인 경우
        if '0' <= c <= '9':
            s.append(c)
        # c가 연산자인 경우
        else:
            num2 = int(s.pop())
            num1 = int(s.pop())
            if c == '+':
                s.append(str(num1 + num2))
            elif c == '-':
                s.append(str(num1 - num2))
            elif c == '*':
                s.append(str(num1 * num2))
            elif c == '/':
                s.append(str(num1 // num2))

    print('#{} {}'.format(tc, int(s.pop())))
    # 후기표기식 출력
    # print(post)



