import sys
sys.stdin = open('input.txt')


# 중위 표기식 -> 후위 표기식
def infix_to_postfix(input_str):
    s = []
    postfix = ''
    op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2}
    for c in input_str:
        # c가 피연산자인 경우
        if '0' <= c <= '9':
            postfix += c
        # c가 연산자인 경우
        else:
            # 스택이 비어있는 경우 바로 스택에 넣어준다.
            if not s:
                s.append(c)
            # 스택이 비어있지 않은 경우
            else:
                # 연산자의 우선순위를 비교한다.
                # 스택의 top의 우선순위 >= c의 우선순위 ---> top을 pop()한다.
                # 스택의 top = s[-1]
                if c == ')':
                    while s[-1] != '(':
                        postfix += s.pop()
                    # '('를 pop()
                    s.pop()
                elif s[-1] != '(' and op_priority[s[-1]] >= op_priority[c]:
                    postfix += s.pop()

                # ')'가 아니고 스택의 top의 우선순위 < c의 우선순위 ---> s에 append()한다.
                if c != ')':
                    s.append(c)
    while s:
        postfix += s.pop()

    return postfix


# 후위표기식 계산
def postfix_calc(postfix):
    s = []
    for c in postfix:
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

    return int(s.pop())


T = 10

for tc in range(1, T+1):
    n = int(input())
    input_str = input()

    postfix = infix_to_postfix(input_str)
    ans = postfix_calc(postfix)

    print('#{} {}'.format(tc, ans))
