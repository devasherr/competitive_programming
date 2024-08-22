class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        res = 0
        for i in range(n):
            dp[i][i] = 1
            res += 1
            if i + 1 < n and s[i] == s[i+1]:
                dp[i][i+1] = 1 
                res += 1
        
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    res += 1
                    
        return res