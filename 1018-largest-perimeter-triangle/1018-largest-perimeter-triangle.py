class Solution:
    def largestPerimeter(self, nums) -> int:
        nums.sort() 
        check = lambda x, y, z: x + y > z and x + z > y and y + z > x
        res = 0

        for i in range(len(nums)-2):
            if check(nums[i], nums[i+1], nums[i+2]):
                res = max(res, nums[i] + nums[i+1] + nums[i+2])
        return res