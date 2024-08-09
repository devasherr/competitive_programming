class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, amount):
            if i == len(nums):
                return 1 if amount == target else 0
            
            for num in nums:
                return backtrack(i+1, amount+nums[i]) + backtrack(i+1, amount-nums[i])
        return backtrack(0, 0)