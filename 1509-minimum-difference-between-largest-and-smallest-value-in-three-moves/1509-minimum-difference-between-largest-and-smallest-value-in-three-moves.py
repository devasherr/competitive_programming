class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: return 0
        n = len(nums)
        nums.sort()
        # 0, 1, 5, 10, 14

        res = float("inf")
        for left in range(4):
            right = 3 - left

            res = min(res, abs(nums[n - right - 1] - nums[left]))
        
        return res