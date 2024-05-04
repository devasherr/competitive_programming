class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        palSet = set()
        def generatePal(c, strList):
            unk = set(strList)

            for u in unk:
                palSet.add(c+u+c)

        count = Counter(s)
        l = 0
        r = l + 2

        while l < len(s) - 2:
            if s[l] == s[r]:
                generatePal(s[l], s[l+1:r])

            r += 1

            if r == len(s):
                l += 1
                r = l + 2

        return len(palSet)