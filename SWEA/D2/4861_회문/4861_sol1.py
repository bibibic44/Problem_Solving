import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = [input() for _ in range(N)]

    def func(s):
        for i in range(M//2):
            if s[i] != s[M-1-i]:
                break
        else:
            return True

        return False


    for i in range(N):
        for j in range(0, N-M+1):
            # 가로
            if func(''.join(a[i][j:M+j])):
                print('#{} {}'.format(tc, ''.join(a[i][j:M+j])))
                break
        # 세로
        else:
            for j in range(0, N-M+1):
                tmp = ''
                for k in range(0, M):
                    tmp += a[j+k][i]
                if func(tmp):
                    print('#{} {}'.format(tc, tmp))
                    break
