class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, res = 0, -1
        target = sum(nums) - x
        cur = 0

        for right in range(len(nums)):
            cur += nums[right]

            while left < len(nums) and cur > target:
                cur -= nums[left]
                left += 1

            if cur == target:
                res = max(res, right - left + 1)

        return len(nums) - res if res != -1 else -1