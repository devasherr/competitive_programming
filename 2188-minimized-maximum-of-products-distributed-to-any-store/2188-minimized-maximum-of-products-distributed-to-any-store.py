class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def calcX(x):
            cur = quantities[0]
            idx = 0

            for _ in range(n):
                if idx >= len(quantities):
                    break
                
                if cur <= x:
                    idx += 1
                    cur = quantities[idx] if idx < len(quantities) else 0
                else:
                    cur -= x

            return idx >= len(quantities)

        left, right = 1, max(quantities)
        res = right

        while left <= right:
            mid = left + (right - left) // 2
            if calcX(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res