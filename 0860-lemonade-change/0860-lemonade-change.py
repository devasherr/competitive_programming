class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                ten += 1
                five -= 1
            elif ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3

        return True if five >= 0 else False