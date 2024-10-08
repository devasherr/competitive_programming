class Solution:
    def minSwaps(self, s: str) -> int:
        off = 0
        open = 0
        for c in s:
            if c == "[":
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    off += 1
        
        return (off + 1) // 2