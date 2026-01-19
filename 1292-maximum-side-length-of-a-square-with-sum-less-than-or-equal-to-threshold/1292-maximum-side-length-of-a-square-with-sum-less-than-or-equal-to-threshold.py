class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                top = mat[i][j-1] if j-1 >= 0 else 0
                left = mat[i-1][j] if i-1 >= 0 else 0
                dig = mat[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0

                mat[i][j] += top + left - dig

        def compute(k):
            for i in range(k, len(mat)):
                for j in range(k, len(mat[0])):
                    top = mat[i][j-k-1] if j-k-1 >= 0 else 0
                    left = mat[i-k-1][j] if i-k-1 >= 0 else 0
                    dig = mat[i-k-1][j-k-1] if i-k-1 >= 0 and j-k-1 >= 0 else 0

                    cur = mat[i][j] - left - top + dig
                    if cur <= threshold:
                        return True
            return False

        res = 0
        left, right = 0, min(len(mat), len(mat[0]))
        while left <= right:
            mid = left + (right - left) // 2
            if compute(mid):
                res = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        return res
