class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # half puls left bound
            mid = l + ((r - l) // 2)

            if nums[mid] > target:
                r -= 1
            elif nums[mid] < target:
                l += 1
            else:
                return mid

        return -1