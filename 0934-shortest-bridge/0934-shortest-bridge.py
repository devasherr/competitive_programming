class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # dfs for starting points
        # bfs for shortest path
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inBound(i, j):
            return 0 <= i < n and 0 <= j < n
        
        visit = set()
        def dfs(i, j):
            if not inBound(i, j) or grid[i][j] == 0 or (i, j) in visit:
                return
            visit.add((i, j))

            for dr, dc in directions:
                dfs(i+dr, j+dc)

        def bfs():
            q = deque(visit)
            level = 0

            while q:
                for _ in range(len(q)):
                    a, b = q.popleft()

                    for dr, dc in directions:
                        if inBound(a+dr, b+dc) and (a+dr, b+dc) not in visit:
                            if grid[a+dr][b+dc] == 1: return level
                            q.append((a+dr, b+dc))
                            visit.add((a+dr, b+dc))
                level += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()