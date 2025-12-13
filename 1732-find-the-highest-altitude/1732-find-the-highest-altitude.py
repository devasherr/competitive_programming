class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        altitide = 0

        for n in gain:
            altitide += n
            res = max(res, altitide)

        return res
