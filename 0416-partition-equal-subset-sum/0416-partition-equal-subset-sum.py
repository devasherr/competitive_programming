class Solution:
    def canPartition(self, nums) -> bool:
        n = sum(nums)
        if n % 2 != 0: return False
        n //= 2

        def find(i, val):
            if i == len(nums): return val == n

            if (i, val) not in memo:
                memo[(i, val)] = find(i+1, val+nums[i]) or find(i+1, val)
            return memo[(i, val)]

        memo = {}
        return find(0, 0)