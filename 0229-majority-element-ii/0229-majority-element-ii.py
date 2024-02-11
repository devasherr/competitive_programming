class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        
        res = []
        for n in countMap.items():
            k, v = n
            if v > len(nums) // 3:
                res.append(k)
        return res