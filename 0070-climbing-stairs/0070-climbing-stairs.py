class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i > n: return 0
            if i == n: return 1

            if i not in memo:
                memo[i] = dp(i+1) + dp(i+2)
            return memo[i]

        memo = {}
        return dp(0)