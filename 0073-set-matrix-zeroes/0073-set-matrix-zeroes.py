class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        firstRow = any([matrix[0][i] == 0 for i in range(cols)])
        firstCol = any([matrix[i][0] == 0 for i in range(rows)])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            if matrix[i][0] != 0: continue
            for j in range(1, cols):
                matrix[i][j] = 0
        for j in range(1, cols):
            if matrix[0][j] != 0: continue
            for i in range(1, rows):
                matrix[i][j] = 0
        
        if firstRow:
            for j in range(cols):
                matrix[0][j] = 0
        if firstCol:
            for i in range(rows):
                matrix[i][0] = 0