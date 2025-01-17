class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 % 2 == 0 and n2 % 2 == 0:
            return 0

        x, y = 0, 0
        for n in nums1:
            x ^= n
        for n in nums2:
            y ^= n
        
        if n1 & 1 and n2 & 1:
            return x ^ y
        
        if n1 % 2 != 0:
            x = 0
        if n2 % 2 != 0:
            y = 0
        return x ^ y