def bfs(g, visited, node):
    q = []
    q.append(node)
    while q:
        now = q.pop(0)
        for x in g[now]:
            if x not in visited:
                q.append(x)
                visited.append(x)
            else:
                return 1


T = int(input())

for tc in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    g = [[] for _ in range(n+1)]

    for i in range(1, n+1):
        g[i].append(nums[i-1])

    cnt = 0
    visited = []
    for i in range(1, n+1):
        if i not in visited:
            visited.append(i)
            cnt += bfs(g, visited, i)

    print(cnt)
