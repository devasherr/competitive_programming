class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        for i in range(len(matrix)):
            rowSet = set()
            colSet = set()
            for j in range(len(matrix[0])):
                rowSet.add(matrix[i][j])
                colSet.add(matrix[j][i])

            if len(rowSet) != len(matrix[0]):
                return False
            if len(colSet) != len(matrix[0]):
                return False
                
        return True