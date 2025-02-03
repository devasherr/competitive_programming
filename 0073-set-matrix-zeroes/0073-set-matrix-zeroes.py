class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet, colSet = set(), set()
        N, M = len(matrix), len(matrix[0])

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        
        for i in rowSet:
            for j in range(M):
                matrix[i][j] = 0
        
        for j in colSet:
            for i in range(N):
                matrix[i][j] = 0
                