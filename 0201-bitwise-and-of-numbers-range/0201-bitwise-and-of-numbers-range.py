class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            count += 1

            left >>= 1
            right >>= 1
        
        return left << count