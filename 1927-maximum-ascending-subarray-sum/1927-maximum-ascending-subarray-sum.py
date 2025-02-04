class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, curSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curSum = 0
            
            curSum += nums[i]
            res = max(res, curSum)
        return res