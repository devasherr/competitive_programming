class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixCount = defaultdict(int)
        prefixCount[0] = 1
        
        nums.insert(0, 0)

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] - k in prefixCount:
                res += prefixCount[nums[i] - k]

            prefixCount[nums[i]] += 1
                
        return res