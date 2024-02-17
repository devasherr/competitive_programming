class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor of same number is 0
        
        xor = 0
        for n in nums:
            xor = xor ^ n
        return xor