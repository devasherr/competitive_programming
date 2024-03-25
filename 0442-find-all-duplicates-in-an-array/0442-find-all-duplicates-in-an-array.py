class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numCount = defaultdict(int)
        res = []

        for n in nums:
            numCount[n] += 1
        for k in numCount:
            if numCount[k] == 2:
                res.append(k)
        return res