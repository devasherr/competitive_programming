class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        numSet = set()

        for n in nums:
            if n < 0:
                numSet.add(n)
        
        for n in nums:
            if n > 0 and (n*-1) in numSet:
                res = max(res, n)

        return res