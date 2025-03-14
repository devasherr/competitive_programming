class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def checkDistribution(val):
            cur = 0
            for i in range(len(candies)):
                cur += candies[i] // val
            return cur >= k

        left, right = 1, sum(candies)
        res = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if checkDistribution(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res