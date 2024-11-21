class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in guards:
            matrix[i][j] = 1
        for i, j in walls:
            matrix[i][j] = 2

        def inBound(i, j):
            return 0 <= i < m and 0 <= j < n

        def traverse(a, b):
            # down
            i = a
            while i < m:
                if matrix[i][b] == 2: break
                matrix[i][b] = 1
                i += 1

            # up
            i = a
            while i >= 0:
                if matrix[i][b] == 2: break
                matrix[i][b] = 1
                i -= 1

            j = b
            # left
            while j >= 0:
                if matrix[a][j] == 2: break 
                matrix[a][j] = 1
                j -= 1

            # right
            j = b
            while j < n:
                if matrix[a][j] == 2: break 
                matrix[a][j] = 1
                j += 1

        for i, j in guards:
            traverse(i, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    res += 1
        return res