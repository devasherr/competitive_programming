class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        totalMax = nums[-1]
        res = 0

        for i in range(len(nums)-1,-1,-1):
            if nums[i] <= totalMax:
                totalMax = nums[i]
                continue
            
            lower = nums[i] // 2
            higher = lower + (nums[i] & 1)
            if higher <= totalMax:
                res += 1
                totalMax = min(totalMax, lower)
            else:
                res += math.ceil(nums[i] / totalMax) - 1
                if nums[i] % totalMax:
                    totalMax = min(totalMax, nums[i] % totalMax)
        return res
