import sys

sys.stdin = open('input.txt')

T = int(input())


# 새로운 트리를 만드는 함수
def make_tree(N, now, tree_list):
    for i in range(N):
        # 마지막 노드에 새로운 입력값을 저장
        if tree_list[now] == -1:
            tree_list[now] = input_val[i]

        # 현재 노드와 부모 노드를 비교하며 거슬러 올라가기 위한 노드 번호 tmp
        tmp_node = now
        parent_node = (tmp_node - 1) // 2
        # 현재 노드가 부모 노드보다 작으면 부모 노드와 swap
        # 부모 노드 번호 = (현재 노드-1) // 2
        while tmp_node != 0 and tree_list[tmp_node] < tree_list[parent_node]:
            tree_list[tmp_node], tree_list[parent_node] = tree_list[parent_node], tree_list[tmp_node]
            tmp_node = parent_node
            parent_node = (parent_node - 1) // 2
        
        # 마지막 노드 번호 갱신
        now += 1


# 조상 노드에 저장된 정수의 합을 구하는 함수
def calc_tree_ancestor(now, cnt):
    # 루트 노드의 값인 tree_list[0]는 cnt에 처음부터 더해져 있었기 때문에 따로 더하지 않아도 된다.
    # 함수 호출 시 cnt에 tree_list[0]가 인수로 전달되었다.
    if now == 0:
        return cnt

    cnt += tree_list[now]
    cnt = calc_tree_ancestor((now-1) // 2, cnt)
    return cnt


for tc in range(1, T + 1):
    N = int(input())
    tree_list = [-1 for _ in range(N)]
    input_val = list(map(int, input().split()))

    # 새로운 트리를 만든다.
    make_tree(N, 0, tree_list)

    # 조상 노드에 저장된 정수의 합을 구한다.
    # 루트 노드의 값은 cnt에 미리 더해둔다.
    cnt = calc_tree_ancestor(((N-1) - 1) // 2, tree_list[0])
    print('#{} {}'.format(tc, cnt))
