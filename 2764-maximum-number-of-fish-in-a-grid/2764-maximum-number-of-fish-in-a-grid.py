class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inBound = lambda i, j: 0 <= i < rows and 0 <= j < cols

        def bfs(i, j):
            val = grid[i][j]
            grid[i][j] = 0
            for dr, dc in directions:
                if inBound(i+dr, j+dc) and grid[i+dr][j+dc]:
                    val += bfs(i+dr, j+dc)
            return val

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    res = max(res, bfs(i, j))
        return res