import sys

sys.stdin = open('input.txt')

T = int(input())


def make_tree(now, tree_list):
    if now >= N:
        return 0
    # 현재 노드에 값이 저장되어 있는 경우 -> 값 리턴
    if tree_list[now] != -1:
        return tree_list[now]
    
    # 현재 노드에 값이 저장되어 있지 않은 경우 -> 자식 노드의 합을 저장
    # 자식 노드 = (현재 노드 * 2) + 1 / (현재 노드 * 2) + 2
    if tree_list[now] == -1:
        tree_list[now] = make_tree(now * 2 + 1, tree_list) + make_tree(now * 2 + 2, tree_list)

    return tree_list[now]


for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 노드를 의미하는 인덱스가 0부터 시작하므로 L -= 1
    L -= 1
    tree_list = [-1 for _ in range(N)]
    for _ in range(M):
        node, num = map(int, input().split())
        # 노드를 의미하는 인덱스가 0부터 시작하므로 node -= 1
        node -= 1
        tree_list[node] = num

    ans = -1
    if tree_list[L] == -1:
        ans = make_tree(L, tree_list)

    print('#{} {}'.format(tc, ans))
