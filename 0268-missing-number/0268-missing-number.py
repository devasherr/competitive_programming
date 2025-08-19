class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)):
            x ^= nums[i]
            
        for i in range(len(nums)+1):
            x ^= i
        return x