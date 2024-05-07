class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            return s[::-1]
        def invert(s):
            res = ""
            for c in s:
                if c == "0":
                    res += "1"
                else:
                    res += "0"
            return res

        prev = "0"
        cur = "0"

        while n > 1:
            cur = prev + "1" + reverse(invert(prev))
            prev = cur

            n -= 1
        
        return cur[k - 1]