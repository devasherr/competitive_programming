class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        def dp(n):
            if n + 1 not in numSet:
                return 1
            if n in memo:
                return memo[n]
            
            memo[n] = 1 + dp(n+1)
            return memo[n]

        memo = {}
        res = 0

        for n in nums:
            res = max(res, dp(n))
        
        return res