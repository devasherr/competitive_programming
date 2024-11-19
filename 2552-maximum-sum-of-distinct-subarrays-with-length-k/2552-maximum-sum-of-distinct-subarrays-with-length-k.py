class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        duplicates = set()
        res, curSum = 0, 0

        left = 0
        for right in range(len(nums)):
            curSum += nums[right]
            count[nums[right]] += 1
            if count[nums[right]] > 1:
                duplicates.add(nums[right])
            
            if right - left + 1 < k: continue
            if not duplicates:
                res = max(res, curSum)
            
            curSum -= nums[left]
            count[nums[left]] -= 1
            if count[nums[left]] == 1:
                duplicates.remove(nums[left])
            left += 1

        return res