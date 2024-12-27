class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                down = dp[i + 1][j] if i + 1 < m else 0
                right = dp[i][j+1] if j + 1 < n else 0
                dp[i][j] += down + right

        return dp[0][0]