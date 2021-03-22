# 백준 코드

n = int(input())
a = list(input())
m = (n+1)//2 - 1
ans = None
for s in range(1<<m):
    ok = True
    for i in range(m-1):
        if (s&(1<<i)) > 0 and (s&(1<<(i+1))) > 0:
            ok = False

    if not ok:
        continue
    b = a[:]
    for i in range(m):
        if (s & (1<<i)) > 0:
            k = 2*i+1
            b[k-1] = '('+b[k-1]
            b[k+1] = b[k+1]+')'
    #print(b)
    c = ''.join(b)
    #print(c)
    temp = eval(c)
    #print(temp)
    if ans is None or ans < temp:
        ans = temp
print(ans)