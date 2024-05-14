class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("inf")

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur = 0
                for idx in range(i, j+1):
                    cur |= nums[idx]

                if cur >= k:
                    res = min(res, j - i + 1)

        return res if res != float("inf") else -1