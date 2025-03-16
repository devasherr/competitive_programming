class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, max(ranks) * (cars ** 2)

        def check(val):
            n = 0
            for r in ranks:
                n += (val / r) ** 0.5 // 1
            return n >= cars

        res = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res