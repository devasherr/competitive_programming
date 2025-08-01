class Solution:
    def climb(self, nums) -> int:
        def dp(i):
            if i >= len(nums): return 0

            if i not in memo:
                memo[i] = min(dp(i+1), dp(i+2)) + nums[i]
            return memo[i]

        memo = {}
        return dp(0)

    def minCostClimbingStairs(self, cost) -> int:
        first = self.climb(cost)
        second = self.climb(cost[1:])

        return min(first, second)
