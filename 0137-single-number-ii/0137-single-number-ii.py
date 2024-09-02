class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single, more = 0, 0
        for n in nums:
            single = (single ^ n) & ~more
            more = (more ^ n) & ~single
        
        return single