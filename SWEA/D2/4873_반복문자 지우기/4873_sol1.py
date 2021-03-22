import sys
sys.stdin = open('input.txt')

T = int(input())

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return

    def top(self):
        if self.stack:
            return self.stack[len(self.stack)-1]
        else:
            return

    def length(self):
        return len(self.stack)


for tc in range(1, T+1):
    input_str = input()
    s = Stack()

    for c in input_str:
        # 스택 s가 비어있으면 push
        if not s:
            s.push(c)
        # 연속된 글자가 아니면 push
        if s.top() != c:
            s.push(c)
        # 연속된 글자인 경우에는 pop
        else:
            s.pop()

    print('#{} {}'.format(tc, s.length()))