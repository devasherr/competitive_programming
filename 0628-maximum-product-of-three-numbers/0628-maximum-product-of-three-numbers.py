class Solution:
    def multiply(self, nums):
        if len(nums) < 3:
            return float("-inf")
        cur = 1
        for n in nums:
            cur *= n
        return cur

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        neg, pos = [], []

        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)
        neg = neg[::-1]
        n = len(nums)
        res = float("-inf")
        res = max(res, self.multiply(neg[:3]))
        res = max(res, self.multiply(pos[-3:]))
        res = max(res, self.multiply(neg[-2:]+pos[-1:]))
        res = max(res, self.multiply(neg[:1]+pos[-2:]))
        return res