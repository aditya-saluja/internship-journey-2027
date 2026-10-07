class Solution:
    def matrixReshape(self, mat, r, c):
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(rows):
            for j in range(cols):
                index = i * cols + j

                new_i = index // c
                new_j = index % c

                result[new_i][new_j] = mat[i][j]

        return result