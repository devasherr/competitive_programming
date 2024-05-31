class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        target = 0
        for n in nums:
            target ^= n
        
        bitIndex = 1
        while not (bitIndex & target):
            bitIndex = bitIndex << 1

        a, b = 0, 0
        for n in nums:
            if n & bitIndex:
                a ^= n
            else:
                b ^= n

        return [a, b]