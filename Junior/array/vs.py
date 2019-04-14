class Solution:
    def isValidSudoku(self, board: list) -> bool:

        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                block = []

            row_repeat = []
            columns_repeat = []
            for j in range(9):
                if (i, j) == (0, 0):
                    continue
                row_num = board[i][j]
                columns_num = board[j][i]
                if row_num != '.':
                    if row_num not in row_repeat:
                        row_repeat.append(row_num)
                    if row_num not in block:
                        block.append(row_num)
                    else:
                        return False

                if columns_num != '.' and columns_num not in columns_repeat:
                    columns_repeat.append(columns_num)
                else:
                    return False
