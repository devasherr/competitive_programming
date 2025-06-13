class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inBound = lambda x, y : 0 <= x < len(image) and 0 <= y < len(image[0])

        q = deque([(sr, sc)])
        original = image[sr][sc]

        while q:
            i, j = q.popleft()
            image[i][j] = color

            for dr, dc in directions:
                if inBound(i+dr, j+dc) and image[i+dr][j+dc] == original and image[i+dr][j+dc] != color:
                    q.append((i+dr, j+dc))
        return image