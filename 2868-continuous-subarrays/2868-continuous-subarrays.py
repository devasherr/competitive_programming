class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left, res = 0, 0
        count = defaultdict(int)

        for right in range(len(nums)):
            count[nums[right]] += 1
            while left < right and max(count) - min(count) > 2:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            res += (right - left + 1)
        return res