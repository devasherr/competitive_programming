class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] += 1
        
        for n in nums:
            idx = abs(n) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0: return i
        return len(nums)