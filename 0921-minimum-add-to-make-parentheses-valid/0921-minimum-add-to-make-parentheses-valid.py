class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        for c in s:
            if c == "(":
                res += 1
            else:
                res -= 1
        return abs(res)