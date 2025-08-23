class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        def canEat(n):
            cur = 0
            for i in range(len(piles)):
                cur += math.ceil(piles[i] / n)
            return cur <= h

        left, right = 1, sum(piles)
        res = 0
        while left <= right:
            mid = left + (right - left) // 2
            if canEat(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
