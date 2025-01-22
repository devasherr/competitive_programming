class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        upper, lower = [], []
        for i in range(len(grid[0])):
            upper.append(grid[0][i])
            lower.append(grid[1][i])
        for i in range(1, len(upper)):
            upper[i] += upper[i-1]
        for i in reversed(range(len(upper) - 1)):
            lower[i] += lower[i+1]
        
        idx, cur = 0, 0
        for i in range(len(upper)):
            if upper[i] + lower[i] > cur:
                cur = upper[i] + lower[i]
                idx = i
        for i in range(len(upper)):
            if idx - i >= 0:
                grid[0][idx-i] = 0
            if idx + i < len(upper):
                grid[1][idx+i] = 0 

        def dp(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return 0
            if (i, j) not in memo:
                down = grid[i][j] + dp(i+1, j)
                right = grid[i][j] + dp(i, j+1)
                memo[(i, j)] = max(down, right)
            return memo[(i, j)]

        memo = {}
        return dp(0, 0)