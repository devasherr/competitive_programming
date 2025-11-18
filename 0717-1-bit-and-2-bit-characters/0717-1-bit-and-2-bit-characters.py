class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        stack = []
        last = False

        # 1 1 1 0
        for c in bits:
            if c == 1:
                if stack:
                    last = False
                    stack.pop()
                    continue
                last = False
                stack.append(c)
                continue

            if stack:
                stack.pop()
                last = False
            else:
                last = True

        return len(stack) > 0 or last
