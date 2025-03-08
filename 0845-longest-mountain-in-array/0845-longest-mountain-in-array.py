class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left, right = deque(), deque()
        leftPrev, rightPrev = arr[0], arr[-1]
        leftCount, rightCount = 0, 0

        for i in range(len(arr)):
            j = len(arr) - i - 1
            
            leftCount = leftCount + 1 if arr[i] > leftPrev else 1
            rightCount = rightCount + 1 if arr[j] > rightPrev else 1

            left.append(leftCount)
            right.append(rightCount)

            leftPrev = arr[i]
            rightPrev = arr[j]

        res = 0
        for i in range(len(arr)):
            if left[i] < 2 or right[i] < 2:
                continue
            
            res = max(res, left[i] + right[i] - 1)
        
        return res