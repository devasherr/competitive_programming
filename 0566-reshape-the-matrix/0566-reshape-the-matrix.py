class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        rows, cols = len(mat), len(mat[0])
        if r * c != rows * cols: return mat

        new_mat = [[0 for _ in range(c)] for _ in range(r)]
        
        line = []
        for i in range(rows):
            for j in range(cols):
                line.append(mat[i][j])

        k = 0
        for i in range(len(new_mat)):
            for j in range(len(new_mat[0])):
                new_mat[i][j] = line[k]
                k += 1

        return new_mat
