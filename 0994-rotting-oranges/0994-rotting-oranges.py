class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        def isInBound(i, j):
            return 0 <= i < rows and 0 <= j < cols
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))

        res = 0
        while q:
            contaminated = False
            for _ in range(len(q)):
                i, j = q.popleft()

                for dr, dc in directions:
                    if isInBound(i+dr, j+dc):
                        if grid[i+dr][j+dc] == 1:
                            q.append((i+dr, j+dc))
                            grid[i+dr][j+dc] = 2
                            contaminated = True

            if contaminated:
                res += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res