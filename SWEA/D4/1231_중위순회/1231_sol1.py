# 재귀로 풀기
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n):
        tmp = input().split()
        tree[int(tmp[0])-1].append(tmp[1])
        for i in range(2, len(tmp)):
            tree[int(tmp[0])-1].append(int(tmp[i])-1)

    def in_order_find_tree(node, words, tree):
        if len(tree[node]) >= 2:
            words = in_order_find_tree(tree[node][1], words, tree)
            words += tree[node][0]
            if len(tree[node]) == 3:
                words = in_order_find_tree(tree[node][2], words, tree)
        else:
            words += tree[node][0]

        return words

    print('#{} {}'.format(tc, in_order_find_tree(0, '', tree)))
