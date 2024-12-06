class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sMap, tMap = {}, {}
        for i in range(len(s)):
            if s[i] in sMap and sMap[s[i]] != t[i]:
                return False
            if t[i] in tMap and tMap[t[i]] != s[i]:
                return False
            sMap[s[i]] = t[i]
            tMap[t[i]] = s[i]
        return True