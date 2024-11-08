class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        nums.append(0)
        res = []

        for i in range(len(nums)-1, 0, -1):
            # remove current index
            xor ^= nums[i]
            res.append(xor ^ (2 ** maximumBit) - 1)
        return res