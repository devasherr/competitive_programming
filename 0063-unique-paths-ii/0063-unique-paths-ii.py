class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        for i in range(n):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        
        if obstacleGrid[0][0] != -1: obstacleGrid[0][0] = 1

        for i in range(n):
            for j in range(n):
                if obstacleGrid[i][j] == -1:
                    continue
                
                if j + 1 < n and obstacleGrid[i][j+1] != -1: obstacleGrid[i][j+1] += obstacleGrid[i][j]
                if i + 1 < n and obstacleGrid[i+1][j] != -1: obstacleGrid[i+1][j] += obstacleGrid[i][j]

        print(obstacleGrid)
        return obstacleGrid[-1][-1] if  obstacleGrid[-1][-1] != -1 else 0