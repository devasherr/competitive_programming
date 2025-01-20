class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[float('inf')] * cols for _ in range(rows)]
        
        heap = [(0, 0, 0)]  # (cost, i, j)
        visited[0][0] = 0
        
        while heap:
            cost, i, j = heappop(heap)
            if i == rows - 1 and j == cols - 1:
                return cost
            
            for k, (dr, dc) in enumerate(directions, 1):
                ni, nj = i + dr, j + dc
                if 0 <= ni < rows and 0 <= nj < cols:
                    new_cost = cost + (1 if k != grid[i][j] else 0)
                    if new_cost < visited[ni][nj]:
                        visited[ni][nj] = new_cost
                        heappush(heap, (new_cost, ni, nj))