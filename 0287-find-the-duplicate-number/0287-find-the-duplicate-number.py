class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cur = nums[0]

        while True:
            if nums[cur] < 0:
                return cur
            
            nums[cur] *= -1
            cur = abs(nums[cur])