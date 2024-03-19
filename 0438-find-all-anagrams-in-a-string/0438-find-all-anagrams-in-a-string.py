class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        res = []
        mainCount = [0] * 26
        for c in p:
            mainCount[ord(c) - ord("a")] += 1
        
        tempCount = [0] * 26
        r = 0

        while r < len(p) - 1:
            tempCount[ord(s[r]) - ord("a")] += 1
            r += 1
        
        l = 0
        while l < len(s) - len(p) + 1:
            tempCount[ord(s[l + len(p) - 1]) - ord("a")] += 1
            if tempCount == mainCount:
                res.append(l)
            tempCount[ord(s[l]) - ord("a")] -= 1
            l += 1

        return res