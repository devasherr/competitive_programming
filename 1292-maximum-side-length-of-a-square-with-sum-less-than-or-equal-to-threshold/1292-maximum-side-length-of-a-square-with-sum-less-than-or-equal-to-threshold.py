class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        # now make some knid of prefix for this

        def canAdd(n):
            for i in range(rows - n + 1):
                for j in range(cols - n + 1):
                    # calc the sum
                    curSum = 0
                    for x in range(n):
                        for y in range(n):
                            curSum += mat[i+x][j+y]
                    if curSum <= threshold:
                        return True
            return False
        
        left, right = 0, min(rows, cols)
        res = 0
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if canAdd(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res