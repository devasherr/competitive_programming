class Solution:
    def minimumReplacement(self, nums) -> int:
        res, bound = 0, nums[-1]
        for i in range(len(nums)-2, -1, -1):
            n = nums[i]
            while n > bound:
                x = math.ceil(n / bound)
                res += x - 1
                n //= x

            bound = n
        return res