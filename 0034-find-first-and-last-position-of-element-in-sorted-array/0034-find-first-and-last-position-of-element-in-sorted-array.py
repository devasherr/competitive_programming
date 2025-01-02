class Solution:
    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
                if nums[mid] == target:
                    res = mid
            else:
                left = mid + 1
        return res

    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
                if nums[mid] == target:
                    res = mid
            else:
                right = mid - 1
        return res
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeft(nums, target), self.searchRight(nums, target)]