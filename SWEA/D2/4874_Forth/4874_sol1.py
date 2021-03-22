import sys
sys.stdin = open('input.txt')

T = int(input())

op = ['+', '-', '*', '/']

for tc in range(1, T+1):
    exp = input().split()
    for i in range(len(exp)):
        if exp[i] != op[0] and exp[i] != op[1] and exp[i] != op[2] and exp[i] != op[3] and exp[i] != '.':
            exp[i] = int(exp[i])

    stack = []
    for i in range(len(exp)):
        if exp[i] == '+':
            if len(stack) == 1:
                print('#{} error'.format(tc))
                break
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)
        elif exp[i] == '-':
            if len(stack) == 1:
                print('#{} error'.format(tc))
                break
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
        elif exp[i] == '*':
            if len(stack) == 1:
                print('#{} error'.format(tc))
                break
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 * num2)
        elif exp[i] == '/':
            if len(stack) == 1:
                print('#{} error'.format(tc))
                break
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 // num2)
        elif exp[i] == '.':
            if len(stack) == 1:
                print('#{} {}'.format(tc, stack.pop()))
            else:
                print('#{} error'.format(tc))
        else:
            stack.append(exp[i])




