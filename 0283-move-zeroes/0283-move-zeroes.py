class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # how about moving all none zero to the right
        
        l = 0
        
        for r in range(len(nums)):  
            if nums[r] != 0:
                temp = nums[r] 
                nums[r] = nums[l] 
                nums[l] = temp
                l += 1

        return nums
             