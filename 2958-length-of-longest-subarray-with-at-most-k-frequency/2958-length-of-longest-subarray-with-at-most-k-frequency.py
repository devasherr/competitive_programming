class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        numCount = defaultdict(int)

        left = 0
        res = 0
        for right in range(len(nums)):
            numCount[nums[right]] += 1

            while numCount[nums[right]] > k:
                numCount[nums[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res