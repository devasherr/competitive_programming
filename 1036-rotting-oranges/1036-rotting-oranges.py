class Solution:
    def orangesRotting(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inBound = lambda i, j: 0 <= i < rows and 0 <= j < cols

        q = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0: return 0 
        
        turns = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc in directions:
                    if inBound(i+dr, j+dc) and grid[i+dr][j+dc] == 1:
                        grid[i+dr][j+dc] = 2
                        q.append((i+dr, j+dc))
                        fresh -= 1
            turns += 1

        if fresh > 0: return -1 
        return turns - 1