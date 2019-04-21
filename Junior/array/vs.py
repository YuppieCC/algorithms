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

    def others(self, board: list) -> bool:
        # 每行的元素以一个字典储存，key是数字，value统一为1.
        dic_row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        # 只遍历一遍整个棋盘
        # 这里比较强大的地方在于它可以通过i,j来推断这个点在哪个3*3网格内
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                not_in_row = num not in dic_row[i]
                not_in_col = num not in dic_col[j]
                not_in_box = num not in dic_box[3 * (i // 3) + (j // 3)]
                if not_in_row and not_in_col and not_in_box:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3 * (i // 3) + (j // 3)][num] = 1  # 利用地板除，向下取余。巧妙地将矩阵划分为九块
                else:
                    return False
        return True


if __name__ == '__main__':
    ip = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s = Solution().others(ip)
    assert s is True, "Test is not pass"
