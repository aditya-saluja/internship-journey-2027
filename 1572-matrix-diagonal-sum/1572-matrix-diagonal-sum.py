class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]              # main diagonal
            total += mat[i][n - 1 - i]      # secondary diagonal

        # center element double count ho gaya tha
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total