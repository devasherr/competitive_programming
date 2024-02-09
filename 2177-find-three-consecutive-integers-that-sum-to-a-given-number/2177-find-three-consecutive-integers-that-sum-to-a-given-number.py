class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # 33 / 3 = 11     -> 10 11 12
        res = []

        if num % 3 == 0:
            leftBound = (num // 3) - 1
            mid = num // 3
            rightBound = (num // 3) + 1

            return ([leftBound, mid, rightBound])

        return []
