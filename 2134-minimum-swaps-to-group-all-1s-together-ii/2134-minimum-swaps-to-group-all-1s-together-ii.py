class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def countZeros(i, j):
            res = 0
            for k in range(i, j):
                if nums[k] == 0:
                    res += 1
            return res

        ones = 0
        for n in nums:
            if n == 1:
                ones += 1

        nums *= 2
        res = float("inf")
        for i in range(len(nums)-ones):
            res = min(res, countZeros(i, i+ones))
        return res