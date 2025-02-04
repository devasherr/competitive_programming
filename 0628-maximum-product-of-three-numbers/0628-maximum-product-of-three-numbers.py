class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = nums[-1] * nums[-2] * nums[-3]

        idx = -1
        for i in range(len(nums)):
            if nums[i] < 0:
                idx = i
        
        if idx > 0:
            res = max(res, nums[0] * nums[1] * nums[-1])
        return res