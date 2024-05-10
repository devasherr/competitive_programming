class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min bound and max bound
        left, right = 1, max(piles)
        res = right

        def canEat(num):
            cur = 0
            for pile in piles:
                cur += ceil(pile/num)

            return cur <= h

        while left <= right:
            mid = left + ((right - left) // 2)

            if canEat(mid):
                right = mid - 1
                res = mid
            else:
                left += 1

        return res