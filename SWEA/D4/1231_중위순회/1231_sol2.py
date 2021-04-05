# 재귀로 풀기: 더 짧은 코드
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    n = int(input())
    tree = [input().split() for _ in range(n)]

    def in_order_find_tree(node, words, tree):
        if len(tree[node]) >= 3:
            words = in_order_find_tree(int(tree[node][2])-1, words, tree)
            words += tree[node][1]
            if len(tree[node]) == 4:
                words = in_order_find_tree(int(tree[node][3])-1, words, tree)
        else:
            words += tree[node][1]

        return words

    print('#{} {}'.format(tc, in_order_find_tree(0, '', tree)))
