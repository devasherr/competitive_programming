class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # perfome the operation
        l = 0

        while l < len(nums) - 1:
            if nums[l] == nums[l + 1]:
                nums[l] *= 2
                nums[l + 1] = 0
            l += 1
        
        # move the zeros
        i = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp

                i += 1
        return nums
