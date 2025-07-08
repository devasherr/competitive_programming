class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] != 0: return -1

        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        inBound = lambda i, j: 0 <= i < rows and 0 <= j < cols
        q = deque([(0, 0, 1)])
        visit = set((0, 0))

        while q:
            i, j, level = q.popleft()
            if i == rows - 1 and j == cols - 1: return  level

            for dr, dc in directions:
                if inBound(i+dr, j+dc) and grid[i+dr][j+dc] == 0 and (i+dr, j+dc) not in visit:
                    q.append((i+dr, j+dc, level+1))
                    visit.add((i+dr, j+dc))
        return -1