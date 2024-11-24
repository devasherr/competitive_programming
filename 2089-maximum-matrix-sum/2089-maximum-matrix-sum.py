class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        totalMin, totalSum, negCount = float("inf"), 0, 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] < 0:
                    negCount += 1
                
                totalSum += abs(matrix[i][j])
                totalMin = min(totalMin, abs(matrix[i][j]))
        
        if negCount % 2 == 0:
            return totalSum
        return totalSum - (2 * totalMin)