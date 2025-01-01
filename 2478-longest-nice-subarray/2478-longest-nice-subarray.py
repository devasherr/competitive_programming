class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        left, cur = 0, nums[0]

        for right in range(1, len(nums)):
            while left < right and cur & nums[right] != 0:
                cur ^= nums[left]
                left += 1
            
            cur |= nums[right]
            res = max(res, right - left + 1)
        return res
       