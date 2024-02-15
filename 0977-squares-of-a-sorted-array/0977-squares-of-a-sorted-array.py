class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(nums) - 1

        while l <= r:
            if (nums[l] ** 2) >= (nums[r] ** 2):
                res.insert(0, nums[l] ** 2)
                l += 1
            else:
                res.insert(0, nums[r] ** 2)
                r -= 1
        return res