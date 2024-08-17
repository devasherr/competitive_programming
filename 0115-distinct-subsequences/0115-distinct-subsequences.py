class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # two points for s and t
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            matched = 0
            if s[i] == t[j]:
                matched = dp(i+1, j+1)
            unmatched = dp(i+1, j)
            memo[(i, j)] = matched + unmatched
            return memo[(i, j)]
            
        memo = {}
        return dp(0, 0)