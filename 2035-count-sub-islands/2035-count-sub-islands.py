class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inBound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        visit = set()

        def dfs(i, j, cur):
            if grid2[i][j] == 0: return
            cur.append((i, j))
            visit.add((i, j))

            for dr, dc in directions:
                if inBound(i+dr, j+dc) and (i+dr, j+dc) not in visit:
                    dfs(i+dr, j+dc, cur)
            return cur

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and (i, j) not in visit:
                    path = dfs(i, j, [])
                    bad = False
                    for x, y in path:
                        if grid1[x][y] == 0:
                            bad = True
                            break
                    if not bad:
                        res += 1

        return res