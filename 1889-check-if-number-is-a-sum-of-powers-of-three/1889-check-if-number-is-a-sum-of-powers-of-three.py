class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = n ** (1/3) // 1

        while p > -1:
            if n - (3 ** p) > -1:
                n -= 3 ** p
            p -= 1
        
        return n == 0