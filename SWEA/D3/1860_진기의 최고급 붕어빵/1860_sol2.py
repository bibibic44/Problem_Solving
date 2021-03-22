# sol1 보다 실행시간이 짧은 코드
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    tmp = list(map(int, input().split()))
    customer = {}
    # key: 손님이 도착한 시간, value: 해당 시간에 도착한 손님의 수
    for i in range(n):
        customer[tmp[i]] = customer.get(tmp[i], 0) + 1
    customer_list = sorted(customer.items())
    bread = 0
    total_cst = 0

    for i in range(len(customer_list)):
        bread = (customer_list[i][0] // m) * k - total_cst

        if bread < customer_list[i][1]:
            print('#{} Impossible'.format(tc))
            break
        else:
            bread -= customer_list[i][1]
            total_cst += customer_list[i][1]

    else:
        print('#{} Possible'.format(tc))
