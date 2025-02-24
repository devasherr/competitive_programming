class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        for i in range(rows):
            left, right = 0, cols - 1
            while left <= right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                if left == right:
                    image[i][left] = 1 - image[i][left]
                    break

                image[i][left] = 1 - image[i][left]
                image[i][right] = 1 - image[i][right]

                left += 1
                right -= 1
        
        return image