import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    check_col = [[False]*9 for _ in range(9)]
    check_row = [[False]*9 for _ in range(9)]
    check_square = [[False]*9 for _ in range(9)]

    def is_sudoku(sudoku):
        for i in range(9):
            for j in range(9):
                # col 확인
                if not check_col[i][sudoku[j][i] - 1]:
                    check_col[i][sudoku[j][i] - 1] = True
                else:
                    return 0
                # row 확인
                if not check_row[i][sudoku[i][j] - 1]:
                    check_row[i][sudoku[i][j] - 1] = True
                else:
                    return 0
                # square 확인
                if not check_square[(i//3) * 3 + j//3][sudoku[i][j] - 1]:
                    check_square[(i//3) * 3 + j//3][sudoku[i][j] - 1] = True
                else:
                    return 0
        return 1

    print('#{} {}'.format(tc, is_sudoku(sudoku)))
