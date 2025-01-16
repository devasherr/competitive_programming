class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bitCount = num2.bit_count()
        res = 0

        i = 31
        while bitCount and i >= 0:
            if num1 & 1 << i:
                res |= 1 << i
                bitCount -= 1
            i -= 1
        
        i = 0
        while bitCount:
            if not num1 & 1 << i:
                res |= 1 << i
                bitCount -= 1
            i += 1
            
        return res