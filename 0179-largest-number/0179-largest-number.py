class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def custom_compare(x, y):
            if x + y > y + x: return -1
            if x + y < y + x: return 1
            return 0

        nums = [str(n) for n in nums]
        nums = sorted(nums, key=functools.cmp_to_key(custom_compare))
        return "0" if nums[0] == "0" else "".join(nums)