import sys
sys.stdin = open('input.txt')

T = int(input())


# 완전 이진 트리 만들기
def make_bin_tree(N, tree):
    for i in range(N):
        # 자식노드번호 = (좌)부모노드번호*2 + 1 / (우)부모노드번호*2 + 2
        node_num = i*2
        if node_num >= N-1:
            break
        tree[i].append(node_num+1)
        if node_num+2 <= N-1:
            tree[i].append(node_num+2)


# 트리 순회(in-order) + 문제 조건에 맞는 트리 만들기
def make_tree(now_node, now_num, tree_list, tree):
    if not tree[now_node]:
        tree_list[now_node] = now_num
        now_num += 1
        return now_num
    for node in tree[now_node]:
        now_num = make_tree(node, now_num, tree_list, tree)
        if tree_list[now_node] == -1:
            tree_list[now_node] = now_num
            now_num += 1
    return now_num


for tc in range(1, T+1):
    N = int(input())
    tree_list = [-1 for _ in range(N)]
    tree = [[] for _ in range(N)]

    # 완전 이진 트리 만들기
    make_bin_tree(N, tree)
    # 문제 조건에 맞추어 트리 만들기
    make_tree(0, 1, tree_list, tree)
    # print(tree_list)
    print('#{} {} {}'.format(tc, tree_list[0], tree_list[(N-2)//2]))
