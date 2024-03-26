class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        def leftSection(i):
            if i - 1 >= 0 and arr[i - 1] < arr[i]:
                return leftSection(i - 1) + 1
            return 0
            
        def rightSection(i):
            if i + 1 < len(arr) and arr[i] > arr[i + 1]:
                return rightSection(i + 1) + 1
            return 0

        res = 0

        # leave first and second to last of checking purpose
        for i in range(1, len(arr) - 1):
            if not (arr[i - 1] < arr[i] > arr[i + 1]):
                continue
            
            res = max(res, leftSection(i) + rightSection(i) + 1)
        return res