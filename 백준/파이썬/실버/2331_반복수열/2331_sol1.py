A, P = map(int, input().split())


def calc(num, p):
    res = 0
    while num > 0:
        res += (num % 10) ** p
        num //= 10

    return res


ans = []
tmp = [A]
while True:
    num = tmp[-1]
    now = calc(num, P)
    if now in tmp:
        idx = 0
        while tmp[idx] != now:
            ans.append(tmp[idx])
            idx += 1
        break
    tmp.append(now)

print(len(ans))
