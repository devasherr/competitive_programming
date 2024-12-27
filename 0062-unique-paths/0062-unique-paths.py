class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.res = 0
        def backtrack(m, n):
            if m < 1 or n < 1:
                return 
            if m == 1 and n == 1:
                self.res += 1
                return
            
            backtrack(m-1, n)
            backtrack(m, n-1)
        
        backtrack(m, n)
        return self.res