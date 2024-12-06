class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)

        for i in range(len(s)):
            if countS[s[i]] != countT[t[i]]:
                return False
        return True