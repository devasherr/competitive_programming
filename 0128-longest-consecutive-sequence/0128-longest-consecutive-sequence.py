class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1

        for val in nums:
            if val - 1 not in nums:
                cur = val
                count = 1

                while cur + 1 in nums:
                    count += 1
                    cur = cur + 1

                res = max(res, count)

        return res

