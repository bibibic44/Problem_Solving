n = int(input())

check_row = [False for _ in range(n)]
check_col = [False for _ in range(n)]
# dig1 = /
check_dig1 = [False for _ in range(2 * n)]
# dig2 = \
check_dig2 = [False for _ in range(2 * n)]


def check(col, row):
    if check_row[row]:
        return False
    if check_col[col]:
        return False
    # 대각선마다 번호를 붙인다. dig1 ===> col+row
    if check_dig1[col+row]:
        return False
    # 대각선마다 번호를 붙인다. dig2 ===> col-row+n
    if check_dig2[col-row+n]:
        return False

    return True


def func(col):
    res = 0
    if col == n:
        return 1
    for row in range(n):
        if check(col, row):
            check_row[row] = check_col[col] = check_dig1[col+row] = check_dig2[col-row+n] = True
            res += func(col + 1)
            check_row[row] = check_col[col] = check_dig1[col+row] = check_dig2[col-row+n] = False

    return res


print(func(0))
