import sys

sys.stdin = open('input.txt')

while True:
    try:
        tc, n = map(int, input().split())
        tmp = list(map(int, input().split()))
    except:
        break

    g = [[] for _ in range(100)]
    for i in range(0, 2*n, 2):
        s, e = tmp[i], tmp[i+1]
        g[s].append(e)

    visited = [False] * 100

    def func(s=0, e=99):
        visited[s] = True
        if s == e:
            return 1
        for node in g[s]:
            if not visited[node]:
                if func(node, e) == 1:
                    return 1
        return 0

    print('#{} {}'.format(tc, func()))
