class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev, res = float("-inf"), 0

        for n in nums:
            if n > prev:
                prev = n
                continue
            
            res += prev - n + 1
            prev += 1
        
        return res