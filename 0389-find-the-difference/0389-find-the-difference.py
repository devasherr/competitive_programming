class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        countS = defaultdict(int)

        for c in t:
            countT[c] = countT[c] + 1
        for c in s:
            countS[c] = countS[c] + 1

        for c in t:
            if c not in countS:
                return c
            if countS[c] != countT[c]:
                return c
        