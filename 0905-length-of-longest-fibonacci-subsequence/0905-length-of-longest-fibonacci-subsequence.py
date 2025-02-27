class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        def binarySearch(idx, target):
            left, right = idx, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1

        res = 0

        for i in range(1, len(arr)):
            for j in range(i):
                prev, idx = arr[j], i
                cur = 2

                while True:
                    target = prev + arr[idx]
                    x = binarySearch(idx + 1, target)
                    if x == -1: break

                    prev = arr[idx]
                    idx = x
                    cur += 1

                res = max(res, cur)
        
        return res if res > 2 else 0