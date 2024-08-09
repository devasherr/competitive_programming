class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
            if n == 0: return 1
            if n < 0: return 0
            if n in memo:
                return memo[n]

            memo[n-1] = self.climbStairs(n-1, memo)
            memo[n-2] = self.climbStairs(n-2, memo)
            return memo[n-1] + memo[n-2]