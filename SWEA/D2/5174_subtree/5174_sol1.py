import sys
sys.stdin = open('input.txt')

T = int(input())


# 서브 트리의 개수를 리턴하는 함수
def subtree_count(now):
    # 현재 노드에 자식 노드가 없으면 1 리턴
    if not tree[now]:
        return 1
    cnt = 0
    # 이진트리의 자식노드를 순회
    for node in tree[now]:
        cnt += subtree_count(node)
    # in-order 방식이므로 root에 해당하는 노드의 개수를 더하기 위해 +1을 해준다.
    return cnt+1


for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+1)]
    tmp = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        root, node = tmp[i], tmp[i + 1]
        tree[root - 1].append(node - 1)

    cnt = subtree_count(N-1)
    print('#{} {}'.format(tc, cnt))
