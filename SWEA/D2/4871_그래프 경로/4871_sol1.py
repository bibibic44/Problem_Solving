import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]

    for i in range(e):
        start, end = map(int, input().split())
        graph[start-1].append(end-1)
    s, g = map(int, input().split())
    s -= 1
    g -= 1

    visited = [False] * v

    def func(s, g):
        res = 0
        visited[s] = True
        if s == g:
            return 1
        for node in graph[s]:
            if not visited[node]:
                visited[node] = True
                if node == g:
                    return 1
                res = func(node, g)
                if res == 1:
                    return res

        return res

    print('#{} {}'.format(tc, func(s, g)))
