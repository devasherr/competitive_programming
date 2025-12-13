class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        nums.sort()
        if len(nums) < 3: return nums[-1]
        return nums[-3]
