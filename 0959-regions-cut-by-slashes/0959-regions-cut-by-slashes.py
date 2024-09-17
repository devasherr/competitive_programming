class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # one scale simply does not work
        # two scale does not expost all diagonal spaces
        # three scale is good enough

        oldRow, oldCol = len(grid), len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # scale the grid 3X
        newRow, newCol = 3 * oldRow, 3 * oldCol 
        newGrid = [[0 for _ in range(newCol)] for _ in range(newRow)]

        for i in range(oldRow):
            for j in range(oldCol):
                r, c = i*3, j*3
                if grid[i][j] == "\\":
                    newGrid[r][c] = 1
                    newGrid[r+1][c+1] = 1
                    newGrid[r+2][c+2] = 1
                elif grid[i][j] == "/":
                    newGrid[r][c+2] = 1
                    newGrid[r+1][c+1] = 1
                    newGrid[r+2][c] = 1
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == newRow or c == newCol or newGrid[r][c] != 0 or (r, c) in visit:
                return
            visit.add((r, c))

            for dr, dc in directions:
                dfs(r+dr, c+dc)                

        visit = set()
        res = 0
        for i in range(newRow):
            for j in range(newCol):
                if newGrid[i][j] == 0 and (i, j) not in visit:
                    dfs(i, j)
                    res += 1
        
        return res