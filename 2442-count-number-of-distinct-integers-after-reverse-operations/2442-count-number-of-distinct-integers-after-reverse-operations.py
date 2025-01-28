class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique = set(nums)
        
        def reverse(n):
            cur = 0
            while n:
                cur *= 10
                cur += n % 10
                n //= 10
            
            unique.add(cur)
        
        for n in nums:
            reverse(n)
        
        return len(unique)