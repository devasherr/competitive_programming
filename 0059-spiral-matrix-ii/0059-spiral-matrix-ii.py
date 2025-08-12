class Solution:
    def generateMatrix(self, n: int):
        mat = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inBound = lambda i, j: 0 <= i < n and 0 <= j < n
        
        k, val = 0, 1
        limit = math.ceil(n / 2)

        while k < limit:
            i, j = k, k
            mat[i][j] = val
            val += 1


            for dr, dc in directions:
                while inBound(i+dr, j+dc) and mat[i+dr][j+dc] == 0:
                    mat[i+dr][j+dc] = val
                    i += dr
                    j += dc
                    val += 1

            k += 1

        return mat