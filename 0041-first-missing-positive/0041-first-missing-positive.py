class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # clean
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # -neg index
        for i in range(n):
            num = abs(nums[i])
            if num == n + 1:
                continue

            nums[num-1] *= -1
               
        # find
        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n + 1