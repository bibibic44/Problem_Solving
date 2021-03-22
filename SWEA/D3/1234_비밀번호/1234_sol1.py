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

    def show(self):
        return self.data[:]


for tc in range(1, T+1):
    n, tmp = input().split()
    n = int(n)

    s = Stack()
    for c in tmp:
        # 스택 s가 비어있으면 push
        if s.is_empty():
            s.push(c)
        # 연속된 글자가 아니면 push
        elif s.top() != c:
            s.push(c)
        # 연속된 글자면 pop
        else:
            s.pop()

    print('#{} {}'.format(tc, ''.join(s.show())))
