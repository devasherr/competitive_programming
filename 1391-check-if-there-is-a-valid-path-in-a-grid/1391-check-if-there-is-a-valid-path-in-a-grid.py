class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # path map
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def isInBound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        pathMap = {
            1: ["left", "right"],
            2: ["up", "down"],
            3: ["left", "down"],
            4: ["down", "right"],
            5: ["left", "up"],
            6: ["up", "right"]
        }

        oppositeMap = { "left": "right", "right": "left", "up": "down","down": "up"}
        self.res = False

        def dfs(i, j, cameFrom):
            if not isInBound(i, j) or (i, j) in visit:
                return False
            if oppositeMap[cameFrom] not in pathMap[grid[i][j]]:
                return False
            if i == rows - 1 and j == cols -1:
                self.res = True
                return True
            
            cur = grid[i][j]
            visit.add((i, j))
            if cur == 1:
                dfs(i, j+1, "left")
                dfs(i, j-1, "right")
            elif cur == 2:
                dfs(i-1, j, "up")
                dfs(i+1, j, "down")
            elif cur == 3:
                dfs(i, j-1, "left")
                dfs(i+1, j, "down")
            elif cur == 4:
                dfs(i, j+1, "right")
                dfs(i+1, j, "down")
            elif cur == 5:
                dfs(i-1, j, "up")
                dfs(i, j-1, "left")
            else:
                dfs(i-1, j,"up")
                dfs(i, j+1, "right")
        
        
        start = oppositeMap[pathMap[grid[0][0]][0]]
        dfs(0, 0, start)
        return self.res