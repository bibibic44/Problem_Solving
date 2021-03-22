import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def is_empty(self):
        return not bool(len(self.data))

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            return None

    # 삭제 없이 단순히 맨 앞의 data 값을 리턴
    def get_front(self):
        if not self.is_empty():
            return self.data[0]
        else:
            return None

    # 삭제 없이 단순히 맨 뒤의 data 값을 리턴
    def get_rear(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return None

    def __repr__(self):
        return '{}'.format(self.data)


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

    q = Queue()
    visited_node_bfs = []

    def bfs(v):
        q.enqueue(v)
        visited_node_bfs.append(v)
        while not q.is_empty():
            # 큐 --> popleft() or pop(0) / 스택 --> pop()
            x = q.dequeue()
            for node in g[x]:
                if node not in visited_node_bfs:
                    q.enqueue(node)
                    visited_node_bfs.append(node)

    bfs(v)
    print(' '.join(map(str, visited_node_bfs)))
