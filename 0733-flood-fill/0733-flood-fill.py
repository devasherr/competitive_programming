class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        targetColor = image[sr][sc]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def isInBound(i, j):
            return 0 <= i < len(image) and 0 <= j < len(image[0]) 

        def dfs(i, j):
            if image[i][j] != targetColor:
                return

            image[i][j] = color
            
            for dr, dc in directions:
                if isInBound(i+dr, j+dc) and image[i+dr][j+dc] != color:
                    dfs(i+dr, j+dc)
        
        dfs(sr, sc)
        return image