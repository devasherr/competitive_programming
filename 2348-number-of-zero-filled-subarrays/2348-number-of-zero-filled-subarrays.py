class Solution:
    def zeroFilledSubarray(self, nums) -> int:
        res, count = 0, 0
        for n in nums:
            if n != 0:
                res += (count * (count+1) // 2)
                count= 0
                continue
            
            count += 1
        if count != 0:
            res += (count * (count+1) // 2)

        return res