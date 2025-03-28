class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preCount = defaultdict(int)
        preCount[0] = 1

        cur, res = 0, 0
        for i in range(len(nums)):
            cur += nums[i]

            res += preCount[cur - k]
            preCount[cur] += 1
        
        return res