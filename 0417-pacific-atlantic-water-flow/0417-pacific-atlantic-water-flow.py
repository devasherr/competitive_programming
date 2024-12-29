class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inBound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def dfs(i, j, inc):
            matrix[i][j] += inc
            visit.add((i, j))

            for dr, dc in directions:
                if inBound(i+dr, j+dc) and (i+dr, j+dc) not in visit and heights[i][j] <= heights[i+dr][j+dc]:
                    dfs(i+dr, j+dc, inc)
        
        visit = set()
        # pacific
        for j in range(cols):
            if (0, j) not in visit:
                dfs(0, j, 1)
        for i in range(rows):
            if (i, 0) not in visit:
                dfs(i, 0, 1)
        visit.clear()
        
        # atlantic
        for j in range(cols):
            if (rows - 1, j) not in visit:
                dfs(rows-1, j, 2)
        for i in range(rows):
            if (i, cols - 1) not in visit:
                dfs(i, cols-1, 2)
        res = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 3:
                    res.append([i, j])
        return res