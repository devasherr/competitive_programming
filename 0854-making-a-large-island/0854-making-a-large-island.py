class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        indexMatrix = [[0 for _ in range(N)] for _ in range(N)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        inBound = lambda i, j: 0 <= i < N and 0 <= j < N

        countMap = {}
        visit = set()

        def bfs(i, j, idx):
            q = deque([(i, j)])
            visit.add((i, j))
            count = 0

            while q:
                i, j = q.popleft()
                indexMatrix[i][j] = idx

                for dr, dc in directions:
                    if inBound(i+dr, j+dc) and grid[i+dr][j+dc] == 1 and (i+dr, j+dc) not in visit:
                        q.append((i+dr, j+dc))
                        visit.add((i+dr, j+dc))
                count += 1
            return count

        idx = 1
        res = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1 and (i, j) not in visit:
                    val = bfs(i, j, idx)
                    countMap[idx] = val
                    res = max(res, val)
                    idx += 1
        
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1: continue

                candidates = set()
                for dr, dc in directions:
                    if inBound(i+dr, j+dc) and indexMatrix[i+dr][j+dc] != 0:
                        candidates.add(indexMatrix[i+dr][j+dc])
                
                cur = 1
                for c in candidates:
                    cur += countMap[c]
                
                res = max(res, cur)
        return res