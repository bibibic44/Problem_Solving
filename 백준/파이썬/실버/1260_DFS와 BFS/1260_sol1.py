import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, v = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for i in range(m):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)

    g = [sorted(g[i]) for i in range(0, n+1)]

    visited_node_dfs = []

    def dfs(v):
        visited_node_dfs.append(v)
        for node in g[v]:
            if node not in visited_node_dfs:
                dfs(node)

    dfs(v)
    print(' '.join(map(str, visited_node_dfs)))

    q = deque()
    visited_node_bfs = []

    def bfs(v):
        q.append(v)
        visited_node_bfs.append(v)
        while q:
            # 큐 --> popleft() / 스택 --> pop()
            x = q.popleft()
            for node in g[x]:
                if node not in visited_node_bfs:
                    q.append(node)
                    visited_node_bfs.append(node)

    bfs(v)
    print(' '.join(map(str, visited_node_bfs)))
