class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[1] = 0

        for i in range(1, n+1):
            first = True
            for j in range(i+i, n+1, i):
                if first:
                    dp[j] = dp[j - i] + 2
                    first = False
                else:
                    dp[j] = dp[j - i] + 1
        return dp[n]