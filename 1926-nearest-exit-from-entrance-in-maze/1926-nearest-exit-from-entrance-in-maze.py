class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0 ,1), (0, -1)]
        found = False
        def isInBound(i, j):
            return 0 <= i < rows and 0 <= j < cols
        
        q = deque()
        for dr, dc in directions:
            r, c = entrance[0]+dr, entrance[1]+dc
            if isInBound(r, c) and maze[r][c] == ".":
                maze[entrance[0]][entrance[1]] = "+"
                q.append((r, c))
        
        res = 0
        while q:
            res += 1
            found = False
            for _ in range(len(q)):
                i, j = q.popleft()
                maze[i][j] = "+"
                if (i == 0 or i == rows - 1) or (j == 0 or j == cols -1):
                    found = True

                for dr, dc in directions:
                    if isInBound(i+dr, j+dc) and maze[i+dr][j+dc] == ".":
                        q.append((i+dr, j+dc))
            if found:
                break
        
        if not found or res == 0:
            return -1 
        else:
            return res