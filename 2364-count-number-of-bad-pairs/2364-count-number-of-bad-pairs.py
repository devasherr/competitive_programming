class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        goodPair = defaultdict(int)
        
        for i in range(len(nums)):
            goodPair[i - nums[i]] += 1
        
        cur = 0
        for key, val in goodPair.items():
            n = val - 1
            cur += n * (n + 1) // 2

        m = len(nums) - 1
        return m * (m + 1) // 2 - cur