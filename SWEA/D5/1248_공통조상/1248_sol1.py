import sys

sys.stdin = open('input.txt')

T = int(input())


# 노드 now의 조상들을 리스트로 리턴해주는 함수
def find_parent(now):
    parent = []
    while find_root[now] != -1:
        parent.append(find_root[now])
        now = find_root[now]
    return parent


# 서브 트리 개수를 리턴해주는 함수
def subtree_count(now):
    if not tree[now]:
        return 1
    cnt = 0
    for node in tree[now]:
        cnt += subtree_count(node)
    return cnt+1


for tc in range(1, T + 1):
    v, e, node1, node2 = map(int, input().split())
    node1 -= 1
    node2 -= 1
    tree = [[] for _ in range(v)]
    find_root = [-1 for _ in range(v)]
    tmp = list(map(int, input().split()))
    for i in range(0, e * 2, 2):
        root, node = tmp[i], tmp[i + 1]
        tree[root - 1].append(node - 1)
        find_root[node - 1] = root - 1

    # 공통 조상 찾기
    common_ancestor = -1
    parent1 = find_parent(node1)
    parent2 = find_parent(node2)
    for i in range(len(parent1)):
        if parent1[i] in parent2:
            common_ancestor = parent1[i]
            break

    # 서브 트리 개수 찾기
    # cnt=1은 common_ancestor 하나 있는 상태
    cnt = subtree_count(common_ancestor)

    print('#{} {} {}'.format(tc, common_ancestor+1, cnt))
