class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # 2,5,1,3,4,7
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n + i])
        return res