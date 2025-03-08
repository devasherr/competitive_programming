class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left, right = deque(), deque()

        prev, count = arr[0], 0
        for i in range(len(arr)):
            if arr[i] > prev:
                count += 1
            else:
                count = 1
            left.append(count)
            prev = arr[i]
        
        prev, count = arr[-1], 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > prev:
                count += 1
            else:
                count = 1
            right.appendleft(count)
            prev = arr[i]
        
        res = 0
        for i in range(len(arr)):
            if left[i] < 2 or right[i] < 2:
                continue
            
            res = max(res, left[i] + right[i] - 1)
        
        return res