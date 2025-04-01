class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixMod = defaultdict(int)
        prefixMod[0] = 1

        cur, res = 0, 0
        for n in nums:
            cur += n

            res += prefixMod[cur % k]
            prefixMod[cur % k] += 1
        
        return res