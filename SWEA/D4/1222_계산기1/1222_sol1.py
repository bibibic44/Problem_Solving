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


for tc in range(1, T+1):
    n = int(input())
    input_str = input()

    # 중위 표기식 -> 후위 표기식
    s = Stack()
    post = ''
    for c in input_str:
        if '0' <= c <= '9':
            post += c
        else:
            if s.is_empty():
                s.push(c)
            else:
                post += s.pop()
                s.push(c)
    post += s.pop()

    # 계산
    for c in post:
        if '0' <= c <= '9':
            s.push(c)
        else:
            num2 = int(s.pop())
            num1 = int(s.pop())
            s.push(str(num1 + num2))

    print('#{} {}'.format(tc, int(s.pop())))


