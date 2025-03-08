class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 3,s1,i2,p3,2,ej1,1,i2,3,4,5,4,3,2,1
        # 5 
        # startMin = 1
        if len(arr) < 3:
            return 0
            
        j = 0
        i = 0
        n = len(arr)
        startMin = 0
        peak = 0
        endMin = 0
        mountain = 0
        # get start min
        while i < n:
            i = j + 1
            while i < n:
                if arr[i] <= arr[i - 1]:
                    startMin = i
                    break
                i += 1

            # get peak
            j = startMin
            while j + 1 < n and arr[j] < arr[j + 1]:
                j += 1
            peak = j

            # get end min
            while j + 1 < n and arr[j] > arr[j + 1]:
                j += 1
            endMin = j
            mountain = max(mountain, j - i + 1)

        return endMin - startMin + 1 if endMin != startMin else 0