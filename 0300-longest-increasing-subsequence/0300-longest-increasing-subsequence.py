class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.res = 0
        def dp(i, prevNum, count):
            if i == len(nums):
                self.res = max(self.res, count)
                return 
            
            if nums[i] > prevNum:
                dp(i+1, nums[i], count+1)
            dp(i+1, nums[i], count)
        dp(0, -1, 0)
        return self.res