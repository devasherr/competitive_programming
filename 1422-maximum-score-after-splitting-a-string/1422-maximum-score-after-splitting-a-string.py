class Solution:
    def maxScore(self, s: str) -> int:
        # turn into list
        nums = [int(c) for c in s]
        # get there total sum
        totalSum = sum(nums)

        left = 0
        right = totalSum
        res = 0

        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                left += 1

            right -= nums[i]
            res = max(res, left + right)
            i += 1

        return res