class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 0
        m = len(nums)

        while n < m:
            nums.append(nums[n])
            n += 1

        return nums
        