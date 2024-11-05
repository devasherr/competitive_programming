class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        prev = None

        for i in range(len(s)):
            if not prev:
                prev = s[i]
                continue
            
            if s[i] != prev:
                res += 1
            prev = None
        
        return res