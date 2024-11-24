class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        for i in range(rows):
            last = cols - 1
            for j in reversed(range(cols)):
                if box[i][j] == "#":
                    box[i][j], box[i][last] = box[i][last], box[i][j]
                    last -= 1
                elif box[i][j] == "*":
                    last = j - 1

        res = [["" for _ in range(rows)] for _ in range(cols)]
        for j in range(cols):
            for i in range(rows):
                res[j][rows - i - 1] = box[i][j]
                
        return res