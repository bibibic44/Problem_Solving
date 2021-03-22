import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    g = [[] for _ in range(v+1)]
    for i in range(e):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)
    s, e = map(int, input().split())

    q = []
    q.append(s)
    visited = [0 for _ in range(v+1)]
    while q:
        node = q.pop(0)
        for x in g[node]:
            if not visited[x]:
                visited[x] = visited[node] + 1
                if x == e:
                    break
                q.append(x)

    print('#{} {}'.format(tc, visited[e]))
