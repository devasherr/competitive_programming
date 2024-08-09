class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, amount, memo):
            if i == len(nums):
                return 1 if amount == target else 0
            
            if (i, amount) in memo:
                return memo[(i,amount)]

            for num in nums:
                memo[(i, amount)] = backtrack(i+1, amount+nums[i], memo) + backtrack(i+1, amount-nums[i], memo)
                return memo[(i, amount)]
        return backtrack(0, 0, {})