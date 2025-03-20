class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        def check(t):
            ans = 0
            for i in range(1, len(t)):
                if t[i] == t[i-1]:
                    ans += 1
            return ans < 2

        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if check(s[i:j]):
                    res = max(res, j - i)
        
        return res