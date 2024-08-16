class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(100)] for _ in range(100)]

        dp[0][0] = poured
        for i in range(100):
            for j in range(100):
                if dp[i][j] > 1:
                    overflow = dp[i][j] - 1
                    dp[i][j] = 1

                    if i+1 < 100: dp[i+1][j] += overflow / 2
                    if i+1 < 100 and j+1 < 100: dp[i+1][j+1] += overflow / 2

        return dp[query_row][query_glass]