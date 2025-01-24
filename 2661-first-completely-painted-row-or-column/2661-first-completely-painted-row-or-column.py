class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        rowCount = [0 for _ in range(row)]
        colCount = [0 for _ in range(col)]

        indexMap = {}
        for i in range(row):
            for j in range(col):
                indexMap[mat[i][j]] = (i, j)
        
        for idx in range(len(arr)):
            i, j = indexMap[arr[idx]]
            rowCount[i] += 1
            colCount[j] += 1

            if rowCount[i] >= col or colCount[j] >= row:
                return idx