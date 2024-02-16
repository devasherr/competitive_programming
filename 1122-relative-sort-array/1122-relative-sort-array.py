class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        countMap = defaultdict(int)
        for n in arr1:
            countMap[n] = countMap[n] + 1

        index = 0
        while index < len(arr2):
            for _ in range(countMap[arr2[index]]):
                res.append(arr2[index])
                arr1.remove(arr2[index])
            index += 1
        
        if len(arr1) > 0:
            arr1.sort()

            for n in arr1:
                res.append(n)
        return res