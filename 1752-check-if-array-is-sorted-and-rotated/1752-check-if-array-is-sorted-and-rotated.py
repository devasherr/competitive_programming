class Solution:
    def check(self, nums: List[int]) -> bool:
        nums.append(nums[0])
        count = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += 1
        
        return count < 2