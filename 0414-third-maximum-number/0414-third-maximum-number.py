import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = [-n for n in set(nums)]
        if len(nums) < 3: return min(nums) * -1

        heapq.heapify(nums)
        res = 0

        for _ in range(3):
            if not nums: break

            res = -1 * heapq.heappop(nums)

        return res
