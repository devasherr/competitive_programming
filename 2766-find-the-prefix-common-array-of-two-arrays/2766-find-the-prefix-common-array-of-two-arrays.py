class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aSet, bSet = set(), set()
        res = [0 for _ in range(len(A))]

        for i in range(len(A)):
            res[i] += (1 if A[i] in bSet else 0)
            res[i] += (1 if B[i] in aSet else 0)
            res[i] += (1 if A[i] == B[i] else 0)

            aSet.add(A[i])
            bSet.add(B[i])
            
        for i in range(1, len(A)):
            res[i] += res[i-1]
        return res