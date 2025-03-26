class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xStack, yStack = [], []
        rectangles.sort()
        xStack.append([rectangles[0][0], rectangles[0][2]])

        for i in range(1, len(rectangles)):
            x1, x2 = rectangles[i][0], rectangles[i][2]
            if x1 < xStack[-1][-1]:
                px1, px2 = xStack.pop()
                xStack.append([min(px1, x1), max(px2, x2)])
            else:
                xStack.append([x1, x2])
        
        rectangles.sort(key = lambda x : x[1])
        yStack.append([rectangles[0][1], rectangles[0][3]])

        for i in range(1, len(rectangles)):
            y1, y2 = rectangles[i][1], rectangles[i][3]
            if y1 < yStack[-1][-1]:
                py1, py2 = yStack.pop()
                yStack.append([min(py1, y1), max(py2, y2)])
            else:
                yStack.append([y1, y2])
        
        print(xStack)
        print(yStack)
        return len(xStack) >= 3 or len(yStack) >= 3