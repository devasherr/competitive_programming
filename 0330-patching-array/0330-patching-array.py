class Solution:
    def minPatches(self, nums, n: int) -> int:
        res, i = 0, 0
        k = 1
        
        while k <= n:
            if i < len(nums) and nums[i] <= k:
                k += nums[i]
                i += 1
            else:
                # patch here
                k += k
                res += 1

        return res