class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) < len(part):
                continue
            
            if "".join(stack[len(stack) - len(part):]) == part:
                for _ in range(len(part)):
                    stack.pop()
        
        return "".join(stack)