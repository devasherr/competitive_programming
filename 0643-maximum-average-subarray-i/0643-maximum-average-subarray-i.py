class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l , r = 0, 0 
        curSum = 0
        while r < k:
            curSum += nums[r]
            r += 1
        
        avg = curSum / k
        while l < len(nums) - k:
            curSum += nums[r] - nums[l]
            l += 1
            r += 1

            avg = max(avg, curSum / k)
        return avg