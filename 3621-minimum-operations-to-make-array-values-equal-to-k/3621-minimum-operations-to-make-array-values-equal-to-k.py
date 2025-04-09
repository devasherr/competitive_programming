class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        
        for n in nums:
            if n < k: return -1
            if n > k:
                count[n] += 1
        
        return len(count)