class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        r = 0
        s = s.strip()
        s += " "
        
        res = []
        while r < len(s):
            while s[r] != " ":
                r += 1
            res.append(s[l:r])
            print(res)

            while r < len(s) and s[r] == " ":
                r += 1
            l = r
        return " ".join(res[::-1])