import sys

sys.stdin = open('input.txt')

T = 10


def calc_tree(now_node, tree):
    if len(tree[now_node]) == 1:
        return tree[now_node][0]

    res = 0
    if tree[now_node][0] == '+':
        res = calc_tree(tree[now_node][1], tree) + calc_tree(tree[now_node][2], tree)
    elif tree[now_node][0] == '-':
        res = calc_tree(tree[now_node][1], tree) - calc_tree(tree[now_node][2], tree)
    elif tree[now_node][0] == '/':
        res = calc_tree(tree[now_node][1], tree) / calc_tree(tree[now_node][2], tree)
    elif tree[now_node][0] == '*':
        res = calc_tree(tree[now_node][1], tree) * calc_tree(tree[now_node][2], tree)

    return res


for tc in range(1, T + 1):
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N):
        input_val = input().split()
        # input_val의 0번째 값은 노드 번호
        if input_val[1] == '+' or input_val[1] == '-' or input_val[1] == '*' or input_val[1] == '/':
            # input_val의 1번째 값이 연산자 -> 2,3번째 값은 각각 자식 노드
            tree[int(input_val[0]) - 1].append(input_val[1])
            tree[int(input_val[0]) - 1].append(int(input_val[2]) - 1)
            tree[int(input_val[0]) - 1].append(int(input_val[3]) - 1)
        # input_val의 1번째 값이 숫자 -> 정점이 양의 정수인 경우
        else:
            tree[int(input_val[0]) - 1].append(int(input_val[1]))

    ans = calc_tree(0, tree)
    ans = int(ans)

    print('#{} {}'.format(tc, ans))

