A, P = map(int, input().split())


def calc(num, p):
    res = 0
    while num > 0:
        res += (num % 10) ** p
        num //= 10

    return res


ans = 0
tmp = [A]
while True:
    num = tmp[-1]
    now = calc(num, P)
    if now in tmp:
        ans = tmp.index(now)
        break
    tmp.append(now)

print(ans)
