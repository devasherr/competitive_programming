class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        openCount = 0
        isOpen = True

        for c in s:
            if c == "(":
                openCount += 1
                isOpen = True
            elif isOpen and c == ")":
                openCount -= 1
                res += (2 ** openCount)
                isOpen = False

        return res