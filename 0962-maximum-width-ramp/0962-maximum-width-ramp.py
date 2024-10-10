class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        futureMax = [n for n in nums]

        for i in range(len(futureMax)-2, -1, -1):
            futureMax[i] = max(futureMax[i], futureMax[i+1])
        
        left, res = 0, 0
        for right in range(len(nums)):
            while left < right and nums[left] > futureMax[right]:
                left += 1
            res = max(res, right - left)
        return res