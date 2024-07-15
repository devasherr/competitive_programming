class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]

        for i in range(1, len(nums)):
            if maxJump == 0:
                return False
                
            maxJump -= 1
            maxJump = max(maxJump, nums[i])

        return True