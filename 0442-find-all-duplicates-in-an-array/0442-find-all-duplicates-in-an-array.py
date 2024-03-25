class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numSet = set()
        res = []

        for n in nums:
            if n in numSet:
                res.append(n)
            else:
                numSet.add(n)
        
        return res