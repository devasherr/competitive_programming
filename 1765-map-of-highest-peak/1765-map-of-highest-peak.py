class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        directions = [(1, 0), (-1, 0), (0, 1),  (0, -1)]
        def isInBound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        q = deque()
        startIndex = set()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    q.append((i, j))
                    startIndex.add((i, j))
        
        level = 1

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for dr, dc in directions:
                    if not isInBound(i+dr, j+dc):
                        continue
                    if (i+dr, j+dc) not in startIndex and isWater[i+dr][j+dc] == 0:
                        isWater[i+dr][j+dc] = level
                        q.append((i+dr, j+dc))   
            level += 1

        return isWater            