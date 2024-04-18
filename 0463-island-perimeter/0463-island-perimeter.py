class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            cur = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    cur += 4

                    if j > 0 and grid[i][j - 1] == 1:
                        cur -= 1
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        cur -= 1
                    if i > 0 and grid[i - 1][j] == 1:
                        cur -= 1
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        cur -= 1
            res += cur
            
        return res