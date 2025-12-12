class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            x = abs(n)
            if nums[x-1] < 0:
                return x

            nums[x-1] *= -1
