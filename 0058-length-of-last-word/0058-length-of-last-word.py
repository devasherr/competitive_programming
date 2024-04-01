class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1

        while True:
            if s[r] != " ":
                break
            r -= 1

        res = 0
        
        while r >= 0:
            if s[r] == " ":
                break

            res += 1
            r -= 1
        
        return res