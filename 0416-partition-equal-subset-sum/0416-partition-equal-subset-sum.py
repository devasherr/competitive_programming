class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if n % 2 != 0: return False

        def dp(i, val):
            if i == len(nums): return val == n // 2

            if (i, val) not in memo:
                memo[(i, val)] = dp(i+1, val+nums[i]) or dp(i+1, val)
            return memo[(i, val)]
        
        memo = {}
        return dp(0, 0)