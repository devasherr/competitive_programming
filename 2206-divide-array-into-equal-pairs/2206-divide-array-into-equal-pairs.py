class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        pairs = 0
        for key in count:
            if count[key] % 2 != 0:
                return False
            pairs += count[key] // 2
        
        return pairs == len(nums)/ 2