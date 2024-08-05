class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def backtrack(m, n, memo):
            if m == 1 and n == 1:
                return 1
            if m < 1 or n < 1:
                return 0
            if (m, n) in memo:
                return memo[(m, n)]
            
            memo[(m-1, n)] = backtrack(m-1, n, memo)
            memo[(m, n-1)] = backtrack(m, n-1, memo)
            return memo[(m-1, n)] + memo[(m, n-1)]
        
        return backtrack(m, n, {})