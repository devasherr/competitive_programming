class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                for j in range(3):
                    nums[i+j] = 1 - nums[i+j]
                res += 1
        
        return res if 0 not in nums else -1