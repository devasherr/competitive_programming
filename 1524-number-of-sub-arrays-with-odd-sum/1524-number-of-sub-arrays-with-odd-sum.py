class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur, res = 0, 0
        odd, even = 0, 0

        for n in arr:
            cur += n
            if cur & 1:
                res += 1
                res += even
                odd += 1
            else:
                res += odd
                even += 1
        
        return res % (10 ** 9 + 7)
