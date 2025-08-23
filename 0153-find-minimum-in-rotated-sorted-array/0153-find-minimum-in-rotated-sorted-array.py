class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                res = nums[mid]
                right = mid - 1
        return int(res)
