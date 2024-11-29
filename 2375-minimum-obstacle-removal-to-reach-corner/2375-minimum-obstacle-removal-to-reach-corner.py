class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inBound(i, j):
            return 0 <= i < rows and 0 <= j < cols
        
        minHeap = [(0, 0, 0)] # weight, i, j
        visit = set()

        while minHeap:
            w, i, j = heapq.heappop(minHeap)
            if (i, j) in visit: continue
            visit.add((i, j))

            if i == rows - 1 and j == cols - 1:
                return w
            
            for dr, dc in directions:
                if inBound(i+dr, j+dc) and (i+dr, j+dc) not in visit:
                    val = 1 if grid[i+dr][j+dc] == 1 else 0
                    heapq.heappush(minHeap, (w+val, i+dr, j+dc))