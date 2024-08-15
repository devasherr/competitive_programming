class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        
        if obstacleGrid[0][0] != -1: obstacleGrid[0][0] = 1

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == -1:
                    continue
                
                if j + 1 < cols and obstacleGrid[i][j+1] != -1: obstacleGrid[i][j+1] += obstacleGrid[i][j]
                if i + 1 < rows and obstacleGrid[i+1][j] != -1: obstacleGrid[i+1][j] += obstacleGrid[i][j]

        print(obstacleGrid)
        return obstacleGrid[-1][-1] if  obstacleGrid[-1][-1] != -1 else 0