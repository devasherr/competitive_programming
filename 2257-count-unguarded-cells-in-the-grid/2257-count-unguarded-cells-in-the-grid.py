class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in guards:
            matrix[i][j] = 1
        for i, j in walls:
            matrix[i][j] = 2

        def traverse(a, b):
            # down
            i = a + 1
            while i < m:
                if matrix[i][b] == 2 or matrix[i][b] == 1: break
                matrix[i][b] = 3
                i += 1

            # up
            i = a - 1
            while i >= 0:
                if matrix[i][b] == 2 or matrix[i][b] == 1: break
                matrix[i][b] = 3
                i -= 1

            j = b - 1
            # left
            while j >= 0:
                if matrix[a][j] == 2 or matrix[a][j] == 1: break 
                matrix[a][j] = 3
                j -= 1

            # right
            j = b + 1
            while j < n:
                if matrix[a][j] == 2 or matrix[a][j] == 1: break 
                matrix[a][j] = 3
                j += 1

        for i, j in guards:
            traverse(i, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res += 1
        return res