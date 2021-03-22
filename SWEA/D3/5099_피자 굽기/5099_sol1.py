import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    pizza = []
    for i in range(m):
        pizza.append([i+1, tmp[i]])
    oven = []
    for i in range(n):
        oven.append(pizza[i])
    pizza_idx = n

    while len(oven) > 1:
        # print(oven)
        idx, cheese = oven.pop(0)
        if cheese == 0:
            if pizza_idx < m:
                oven.append(pizza[pizza_idx])
                pizza_idx += 1
        else:
            cheese //= 2
            if cheese == 0 and pizza_idx < m:
                oven.append(pizza[pizza_idx])
                pizza_idx += 1
            else:
                oven.append([idx, cheese])

    idx, cheese = oven.pop(0)
    print('#{} {}'.format(tc, idx))
