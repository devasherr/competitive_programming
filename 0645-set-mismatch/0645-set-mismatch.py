class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for n in nums:
            if n > 0:
                nums[n - 1] *= -1
        
        for n in nums:
            if n > 0:
                return [n, n + 1]