class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
                res = min(res, nums[mid])

        return res