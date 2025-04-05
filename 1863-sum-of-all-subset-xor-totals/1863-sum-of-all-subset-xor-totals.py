class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def func(i, val):
            if i >= len(nums):
                return val
            
            inc = func(i+1, nums[i] ^ val)
            exc = func(i+1, val)
            return inc + exc
        
        return func(0, 0)