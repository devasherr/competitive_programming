class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countN = {}
        for n in arr:
            countN[n] = countN.get(n, 0) + 1

        unique = []
        for items in countN.items():
            k, v = items

            if v in unique:
                return False
                
            unique.append(v)

        return True

        