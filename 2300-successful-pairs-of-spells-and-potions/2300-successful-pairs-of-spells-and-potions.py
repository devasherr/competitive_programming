class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        res = []
        for s in spells:
            x = math.ceil(success / s)
            idx = bisect.bisect_left(potions, x)

            res.append(len(potions) - idx)

        return res