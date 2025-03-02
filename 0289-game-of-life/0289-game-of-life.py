class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        inBound = lambda i, j : 0 <= i < rows and 0 <= j < cols

        # alive = 1 or 9, dead = 0 or 8
        for i in range(rows):
            for j in range(cols):
                nei = 0
                for dr, dc in directions:
                    if inBound(i+dr, j+dc) and board[i+dr][j+dc] in [1, 8]:
                        nei += 1
                
                if board[i][j] in [0, 9]:
                    if nei == 3:
                        board[i][j] = 9
                    continue
                
                if nei < 2 or nei > 3:
                    board[i][j] = 8

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 9:
                    board[i][j] = 1
                elif board[i][j] == 8:
                    board[i][j] = 0