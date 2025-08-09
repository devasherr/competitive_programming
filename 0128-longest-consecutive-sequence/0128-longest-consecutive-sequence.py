class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums = sorted(list(set(nums)))
        res = 1
    
        i = 1
        while i < len(nums):
            cur = 1
            while i < len(nums) and nums[i] == nums[i-1] + 1:
                cur += 1
                i += 1
            i += 1
            res = max(res, cur)

        return res
