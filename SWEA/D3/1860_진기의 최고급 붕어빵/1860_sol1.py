import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    tmp = list(map(int, input().split()))
    customer = {}
    for i in range(n):
        customer[tmp[i]] = customer.get(tmp[i], 0) + 1
    customer_list = sorted(customer.items())
    bread = 0
    max_time = customer_list[-1][0]
    cst_idx = 0

    for i in range(max_time+1):
        if i != 0 and i % m == 0:
            bread += k

        if i == customer_list[cst_idx][0]:
            bread -= customer_list[cst_idx][1]
            if bread < 0:
                print('#{} Impossible'.format(tc))
                break
            cst_idx += 1
    else:
        print('#{} Possible'.format(tc))
