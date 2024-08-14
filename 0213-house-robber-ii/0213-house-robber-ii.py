class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i, amount, parent):
            print(i, amount, parent)
            if i < 0:
                return amount
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            rob = 0
            if i == 0:
                if parent != len(nums) - 1:
                    rob = dp(i-2, amount+nums[i], max(parent, i))
            else:
                rob = dp(i-2, amount+nums[i], max(parent, i))

            no_rob = dp(i-1, amount, parent)
            memo[(i, amount)] = max(rob, no_rob)
            return memo[(i, amount)]
            
        memo = {}
        return dp(len(nums)-1, 0, -1)