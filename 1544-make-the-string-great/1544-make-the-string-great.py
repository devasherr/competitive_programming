class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isupper() and c.lower() == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
                
        return "".join(stack)