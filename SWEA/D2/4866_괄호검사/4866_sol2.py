# 스택 구현
import sys
sys.stdin = open('input.txt')

T = int(input())

class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return False if len(self.data) else True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return


def func(input_str):
    s = Stack()
    for i in range(len(input_str)):
        if input_str[i] == '(' or input_str[i] == '{' or input_str[i] == '[':
            s.push(input_str[i])
        elif input_str[i] == ')':
            if s.is_empty() or s.pop() != '(':
                return 0
        elif input_str[i] == '}':
            if s.is_empty() or s.pop() != '{':
                return 0
        elif input_str[i] == ']':
            if s.is_empty() or s.pop() != '[':
                return 0
    if not s.is_empty():
        return 0

    return 1


for tc in range(1, T+1):
    input_str = input()
    print('#{} {}'.format(tc, func(input_str)))
