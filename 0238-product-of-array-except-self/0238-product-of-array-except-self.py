class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = nums[:], nums[:]

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i]
        
        res = []
        for i in range(len(nums)):
            prev = left[i-1] if i > 0 else 1
            next = right[i+1] if i < len(nums) - 1 else 1
            res.append(prev * next)
        
        return res