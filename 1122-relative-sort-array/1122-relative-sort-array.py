class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countList = [0 for i in range(max(arr1)+1)]

        for n in arr1:
            countList[n] += 1

        res = []
        for n in arr2:
            for _ in range(countList[n]):
                res.append(n)
            countList[n] = 0
        
        # if any remaining
        for i in range(len(countList)):
            for _ in range(countList[i]):
                res.append(i)

        return res