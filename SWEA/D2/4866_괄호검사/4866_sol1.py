import sys
sys.stdin = open('input.txt')

T = int(input())


def func(input_str):
    s = []
    for i in range(len(input_str)):
        if input_str[i] == '(' or input_str[i] == '{' or input_str[i] == '[':
            s.append(input_str[i])
        # 처음부터 닫는 괄호가 입력된 경우 or 괄호의 짝이 맞지 않는 경우
        elif input_str[i] == ')':
            if not s or s.pop() != '(':
                return 0
        elif input_str[i] == '}':
            if not s or s.pop() != '{':
                return 0
        elif input_str[i] == ']':
            if not s or s.pop() != '[':
                return 0
    # 여는 괄호가 남은 경우
    if s:
        return 0

    return 1


for tc in range(1, T+1):
    input_str = input()
    print('#{} {}'.format(tc, func(input_str)))
