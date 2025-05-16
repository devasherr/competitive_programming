class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canPlant(n):
            cur, cons = 0, 0
            for i in range(len(bloomDay) + 1):
                if i == len(bloomDay):
                    cur += (cons // k)
                    break
                if bloomDay[i] <= n:
                    cons += 1
                    continue
                cur += (cons // k)
                cons = 0
            return cur >= m

        left, right = 0, max(bloomDay)
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if canPlant(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res