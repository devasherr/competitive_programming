class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0

        for i in range(len(nums)):
            s = l = nums[i]
            for j in range(i, len(nums)):
                if nums[j] < s:
                    s = nums[j]
                if nums[j] > l:
                    l = nums[j]

                if abs(s - l) <= limit:
                    res = max(res, j - i + 1)
                
        return res