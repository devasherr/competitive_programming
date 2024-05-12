class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, res = len(grid), []

        def gridMax(k, l):
            curMax = 0

            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    curMax = max(curMax, grid[k][l])

            return curMax

        for i in range(1, n - 1):
            temp_row = []
            for j in range(1, n - 1):
                temp = gridMax(i, j)
                temp_row.append(temp)
                
            res.append(temp_row)

        return res