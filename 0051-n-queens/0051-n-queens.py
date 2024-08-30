class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isInBound(i, j):
            return 0 <= i < n and 0 <= j < n

        def setInvalid(board, i, j):
            a, b = i, j
            # down
            while isInBound(i+1, j):
                board[i+1][j] += 1
                i += 1

            # left diagonal
            i, j = a, b
            while isInBound(i+1, j-1):
                board[i+1][j-1] += 1
                i += 1
                j -= 1
            
            # right diagonal
            i, j = a, b
            while isInBound(i+1, j+1):
                board[i+1][j+1] += 1
                i += 1
                j += 1
            return board

        def backtrack(i, j):
            while isInBound(i, j) and board[i][j]:
                j += 1
            if j == n: return 
            setInvalid(board, i, j)
            board[i][j] = float("inf")
            if i == n - 1:
                return          
            backtrack(i+1, 0)

        def getValidPath(board):
            count = 0
            i, j = 0, 0

            ans = []
            for i in range(n):
                cur = ""
                for j in range(n):
                    if board[i][j] == float("inf"):
                        count += 1
                        cur += "Q"
                    else:
                        cur += "."
                ans.append(cur)
            if count == n:
                return ans
        
        res = []
        for i in range(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            backtrack(0, i)

            # get valid path
            ans = getValidPath(board)
            if ans:
                res.append(ans)

        return res 