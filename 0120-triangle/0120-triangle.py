class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dp(i, j):
            if i == len(triangle): return 0

            if (i, j) not in memo:
                left = triangle[i][j] + dp(i+1, j)
                right = triangle[i][j] + dp(i+1, j+1)
                memo[(i, j)] = min(left, right)

            return memo[(i, j)]
        
        memo = {}
        return dp(0, 0)