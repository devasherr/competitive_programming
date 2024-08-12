class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if text1[j] != text2[i]:
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j -1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])
                else:
                    up = 0 if i - 1 < 0 else dp[i-1][j]
                    left = 0 if j - 1 < 0 else dp[i][j-1]
                    dp[i][j] = min(up, left) + 1
        
        return dp[-1][-1]