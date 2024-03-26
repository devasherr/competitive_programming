class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # make all postive
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # now the question is [1-n]
        for i in range(n):
            num = abs(nums[i])

            # we need all to less than n and be negative
            if num > n:
                continue
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1