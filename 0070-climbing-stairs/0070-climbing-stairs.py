class Solution:
    def climbStairs(self, n: int) -> int:
        def backtrack(n, memo):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            memo[n-1] = backtrack(n-1, memo)
            memo[n-2] = backtrack(n-2, memo)
            return memo[n-1] + memo[n-2]
        
        return backtrack(n, {})