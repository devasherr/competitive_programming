class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x, y = sorted(rectangles), sorted(rectangles, key = lambda x: x[1])
        xPrev, yPrev = [x[0][0], x[0][2]], [y[0][1], y[0][3]]
        xCount, yCount = 1, 1

        for i in range(1, len(rectangles)):
            x1, x2 = x[i][0], x[i][2]
            y1, y2 = y[i][1], y[i][3]

            if x1 < xPrev[-1]:
                xPrev = [min(xPrev[0], x1), max(xPrev[1], x2)]
            else:
                xPrev = [x1, x2]
                xCount += 1

            if y1 < yPrev[-1]:
                yPrev = [min(yPrev[0], y1), max(yPrev[1], y2)]
            else:
                yPrev = [y1, y2]
                yCount += 1
        
        return xCount >= 3 or yCount >= 3