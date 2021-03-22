# 중위표기식 ---> 후위표기식 ---> 후위표기식 계산
# Stack 클래스 구현
import sys
sys.stdin = open('input.txt')

T = 10


class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return False if self.data else True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.data.pop()

    def top(self):
        if self.is_empty():
            return
        else:
            return self.data[-1]

    def stack_print(self):
        return self.data


for tc in range(1, T+1):
    n = int(input())
    input_str = input()

    # 중위 표기식 -> 후위 표기식
    s = Stack()
    post = ''
    op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2}
    for c in input_str:
        # c가 피연산자인 경우
        if '0' <= c <= '9':
            post += c
        # c가 연산자인 경우
        else:
            if s.is_empty():
                s.push(c)
            else:
                # ')'가 등장하면 '('가 나올때까지 s를 pop()한다.
                if c == ')':
                    while s.top() != '(':
                        post += s.pop()
                    # '('를 pop()한다. 후위표기식에는 괄호를 넣지 않는다.
                    s.pop()
                # 연산자의 우선순위를 비교한다.
                # s.top()보다 새로운 연산자의 우선순위가 같거나 낮으면 ---> s.top()을 pop()한다.
                elif s.top() != '(' and op_priority[s.top()] >= op_priority[c]:
                    post += s.pop()
                # ')'를 제외한 연산자는 push()한다.
                if c != ')':
                    s.push(c)
    while s.data:
        post += s.pop()

    # 후위표기식 계산
    for c in post:
        # c가 피연산자인 경우
        if '0' <= c <= '9':
            s.push(c)
        # c가 연산자인 경우
        else:
            num2 = int(s.pop())
            num1 = int(s.pop())
            if c == '+':
                s.push(str(num1 + num2))
            elif c == '-':
                s.push(str(num1 - num2))
            elif c == '*':
                s.push(str(num1 * num2))
            elif c == '/':
                s.push(str(num1 // num2))

    print('#{} {}'.format(tc, int(s.pop())))
    # 후기표기식 출력
    # print(post)



