class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i, cur):
            if i == len(nums):
                return cur == target

            add = dp(i+1, cur+nums[i])
            sub = dp(i+1, cur-nums[i])

            return add + sub

        return dp(0, 0)