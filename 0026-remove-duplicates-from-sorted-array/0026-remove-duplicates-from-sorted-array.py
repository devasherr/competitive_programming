class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
       
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left += 1

        return left + 1