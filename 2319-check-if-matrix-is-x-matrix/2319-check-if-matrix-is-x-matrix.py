class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == i or j == len(grid[0]) - i - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
                        
        return True