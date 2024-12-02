class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inBound(i, j):
            return 0 <= i < rows and 0 <= j < cols
        q = deque()
        visit = set()

        def bfs(i, j):
            q.append((i, j))
            visit.add((i, j))

            while q:
                a, b = q.popleft()
                
                for dr, dc in directions:
                    if inBound(a+dr, b+dc) and grid[a+dr][b+dc] == 0 and (a+dr, b+dc) not in visit:
                        q.append((a+dr, b+dc))
                        visit.add((a+dr, b+dc))

        # mark off bad zeros
        for i in range(rows):
            if grid[i][0] == 0: bfs(i, 0)
            if grid[i][cols - 1] == 0: bfs(i, cols -1)
        for j in range(cols):
            if grid[0][j] == 0: bfs(0, j)
            if grid[rows - 1][j] == 0: bfs(rows - 1, j)
        
        # count good connected zeros
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0  and (i, j) not in visit:
                    bfs(i, j)
                    res += 1
        return res