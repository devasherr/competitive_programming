class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        
        res = []
        for candy in candies:
            if candy + extraCandies >= greatest:
                res.append(True)
                continue
            res.append(False)

        return res