class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def backtrack(i, aSum, bSum):
            if i == len(nums):
                return aSum == bSum
                
            return backtrack(i+1, aSum+nums[i], bSum) or backtrack(i+1, aSum, bSum+nums[i])
        return backtrack(0, 0, 0)