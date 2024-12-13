class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            if n - 1 in numSet:
                continue
            
            i = 1
            cur = n
            while cur + 1 in numSet:
                cur += 1
                i += 1
            
            res = max(res, i)
        return res