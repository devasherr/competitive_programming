class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        leftMax, rightMax = nums[:], nums[:]

        for i in range(1, len(nums)):
            leftMax[i] = max(leftMax[i], leftMax[i-1])
        for j in range(len(nums) - 2, -1, -1):
            rightMax[j] = max(rightMax[j], rightMax[j+1])
        
        res = 0
        for j in range(1, len(nums) - 1):
            res = max(res, (leftMax[j-1] - nums[j]) * rightMax[j+1])
        
        return res