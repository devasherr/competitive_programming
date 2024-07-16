class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0

        for _ in range(k):
            if numOnes:
                numOnes -= 1
                res += 1
                continue

            if numZeros:
                numZeros -= 1
                continue
            
            res -= 1

        return res