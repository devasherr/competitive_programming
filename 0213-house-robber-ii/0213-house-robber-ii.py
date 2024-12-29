class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.robStreet(nums[:-1]), self.robStreet(nums[1:]))

    def robStreet(self, street):
        def dfs(i):
            if i >= len(street): return 0
            if i not in memo:
                rob = street[i] + dfs(i+2)
                norob = dfs(i+1)
                memo[i] = max(rob, norob)

            return memo[i]

        memo = {}
        return dfs(0)