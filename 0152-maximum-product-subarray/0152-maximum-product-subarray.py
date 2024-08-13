class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            cur = 1
            for j in range(i, len(nums)):
                cur *= nums[j]
                res = max(res, cur)
        
        return res