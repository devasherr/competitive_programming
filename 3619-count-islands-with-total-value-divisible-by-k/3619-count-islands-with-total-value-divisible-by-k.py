class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inBound = lambda x, y : 0 <= x < len(grid) and 0 <= y < len(grid[0]) 

        def dfs(i, j):
            if not inBound(i, j) or grid[i][j] == 0: return 0

            cur = grid[i][j]
            grid[i][j] = 0
            for dr, dc in directions:
                cur += dfs(i+dr, j+dc)
            return cur

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]: continue
                
                if dfs(i, j) % k == 0:
                    res += 1
        return res
