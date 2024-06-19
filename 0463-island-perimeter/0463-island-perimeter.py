class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isInBound(i, j):
            return 0 <= i < rows and 0 <= j < cols
        
        def dfs(i, j):
            if not isInBound(i, j) or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            count = 0
            for direction in directions:
                count += dfs(i + direction[0], j + direction[1])

            return count
        
        # find start of island
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)