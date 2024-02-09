class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)

        for i in range(len(nums) + 1):
            if i not in numSet:
                return i
                