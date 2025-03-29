class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #  |
        # 1,0,2,3,0,4,5,0

        res = []
        i = 0

        while len(res) < len(arr):
            if arr[i] != 0:
                res.append(arr[i])
            else:
                res.append(0)
                res.append(0)
            i += 1
        
        for i in range(len(arr)):
            arr[i] = res[i]