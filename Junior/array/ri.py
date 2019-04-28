class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 先变换最外层，逐渐向内深入

        ml = len(matrix)
        for i in range(ml):
            for j in range(i + 1, ml):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        # matrix[:] = map(list, zip(*matrix[::-1]))
        # print(matrix)


# unsolved

if __name__ == '__main__':
    ip = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(ip)
