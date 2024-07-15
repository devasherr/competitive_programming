class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curSum = float("-inf")
        left = 0

        for right in range(len(nums)):
            if curSum < 1:
                left = right
                curSum = 0

            curSum += nums[right]
            res = max(res, curSum)

        return res