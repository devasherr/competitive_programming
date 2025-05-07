class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calcResult(n):
            cur = 0
            for v in nums:
                cur += ceil(v/n)
            return cur
        
        left, right = 1, max(max(nums), threshold)
        res = None

        while left <= right:
            mid = left + (right - left) // 2
            if calcResult(mid) <= threshold:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res