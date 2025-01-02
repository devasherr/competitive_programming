class Solution:
    def canCarry(self, weights, k, days):
        cur, count = 0, 1
        for w in weights:
            if w > k: return False
            if cur + w > k:
                count += 1
                cur = 0
            cur += w
        
        return count <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = 0, sum(weights)
        res = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            val = self.canCarry(weights, mid, days)
            if val:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        
        return res