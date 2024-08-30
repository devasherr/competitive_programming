class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific = [[0 for _ in range(cols)] for _ in range(rows)]
        atlantic = [[0 for _ in range(cols)] for _ in range(rows)]

        def isInBound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        q  = deque()
        visit = set()
        # pacific start point
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            visit.add((i, j))
            pacific[i][j] |= 1

            for dr, dc in directions:
                if isInBound(i+dr, j+dc) and (i+dr, j+dc) not in visit and heights[i+dr][j+dc] >= heights[i][j]:
                    q.append((i+dr, j+dc))
        
        q  = deque()
        visit = set()
        # atlantic start point
        for i in range(rows):
            for j in range(cols):
                if i == rows - 1 or j == cols - 1:
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            visit.add((i, j))
            atlantic[i][j] |= 1

            for dr, dc in directions:
                if isInBound(i+dr, j+dc) and (i+dr, j+dc) not in visit and heights[i+dr][j+dc] >= heights[i][j]:
                    q.append((i+dr, j+dc))
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        
        return res