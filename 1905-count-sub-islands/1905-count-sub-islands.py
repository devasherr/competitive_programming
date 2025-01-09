class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inBound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        visit = set()

        def dfs(i, j):
            if grid2[i][j] == 0: return
            good = True
            if grid1[i][j] == 0:
                good = False
            visit.add((i, j))

            for dr, dc in directions:
                if inBound(i+dr, j+dc) and grid2[i+dr][j+dc] == 1 and  (i+dr, j+dc) not in visit:
                    good &= dfs(i+dr, j+dc)
            return good

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and (i, j) not in visit:
                    res += dfs(i, j)
        return res