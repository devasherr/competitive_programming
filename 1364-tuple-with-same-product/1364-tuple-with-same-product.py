class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                count[nums[i] * nums[j]] += 1
            
        res = 0
        for key, val in count.items():
            if val > 1:
                x = val - 1
                res += x * (x+1) // 2

        return res * 8