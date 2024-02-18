class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        indexS = []
        indexT = []

        for i in range(len(s)):
            indexS.append(s.index(s[i]))
            indexT.append(t.index(t[i]))
            
        return indexS == indexT