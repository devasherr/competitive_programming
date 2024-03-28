class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            # leading negative is a burden
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSum = max(maxSum, curSum)
            
        return maxSum