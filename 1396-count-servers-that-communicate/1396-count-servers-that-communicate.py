class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = set()
        for i in range(len(grid)):
            cur = 0
            temp = []
            for j in range(len(grid[0])):
                if grid[i][j]:
                    temp.append((i, j))
                cur += grid[i][j]
            if cur > 1:
                for a, b in temp:
                    res.add((a, b))
                    
        for j in range(len(grid[0])):
            cur = 0
            temp = []
            for i in range(len(grid)):
                if grid[i][j]:
                    temp.append((i, j))
                cur += grid[i][j]
            if cur > 1:
                for a, b in temp:
                    res.add((a, b))

        return len(res)