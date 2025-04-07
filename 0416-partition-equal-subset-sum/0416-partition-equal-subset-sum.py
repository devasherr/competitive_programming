class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def backtrack(i, aSum, bSum, memo):
            if i == len(nums):
                return aSum == bSum

            if (aSum, bSum) in memo:
                return memo[(aSum, bSum)]

            memo[(aSum, bSum)] = backtrack(i+1, aSum+nums[i], bSum, memo) or backtrack(i+1, aSum, bSum+nums[i], memo)
            return memo[(aSum, bSum)]
            
        return backtrack(0, 0, 0, {})