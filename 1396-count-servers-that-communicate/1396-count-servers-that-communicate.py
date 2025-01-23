class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowCount, colCount = [], []
        for i in range(len(grid)):
            rowCount.append(sum(grid[i]))
        for j in range(len(grid[0])):
            cur = 0
            for i in range(len(grid)):
                cur += grid[i][j]
            colCount.append(cur)
            
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if max(rowCount[i], colCount[j]) > 1:
                    res += grid[i][j]
        
        return res