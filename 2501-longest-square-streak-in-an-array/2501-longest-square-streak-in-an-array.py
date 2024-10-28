class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ss = set(nums)
        res = -1

        for n in nums:
            cur = n
            count = 1

            for _ in range(5):
                cur = cur ** 2
                if cur not in ss:
                    break
                count += 1

            res = max(res, count)
        return res if res > 1 else -1 