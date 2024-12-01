class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        double = set(arr)
        zeros = arr.count(0)
        
        for n in arr:
            if n == 0 and zeros == 1: continue
            if n * 2 in double: return True
        return False