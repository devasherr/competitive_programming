class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        minRow = set()
        maxCol = set()

        for i in range(len(matrix)):
            mi = float("inf")
            for j in range(len(matrix[0])):
                mi = min(mi, matrix[i][j])
            minRow.add(mi)

        for i in range(len(matrix[0])):
            ma = float("-inf")
            for j in range(len(matrix)):
                ma = max(ma, matrix[j][i])
            maxCol.add(ma)
        
        for n in minRow:
            if n in maxCol:
                res.append(n)
        return res