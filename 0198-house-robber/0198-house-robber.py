class Solution:
    def rob(self, nums: List[int]) -> int:
        def robChoice(i, memo):
            if i >= len(nums): return 0
            
            if i not in memo:
                memo[i] = max(robChoice(i+2, memo) + nums[i], robChoice(i+1, memo))
            return memo[i]
        return robChoice(0, {})