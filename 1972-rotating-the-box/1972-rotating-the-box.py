class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            count = 0
            for j in range(cols):
                if box[i][j] == "*":
                    count = 0
                    matrix[i][j] = "*"
                    continue
                
                if box[i][j] == "#":
                    count += 1
                if j - 1 >= 0 and matrix[i][j - 1] != "*":
                    matrix[i][j - 1] = 0
                matrix[i][j] = count

        res = [[0 for _ in range(rows)] for _ in range(cols)]
        output = [["." for _ in range(rows)] for _ in range(cols)]

        for j in range(cols):
            for i in range(rows):
                res[j][rows - i - 1] = matrix[i][j]

        for i in range(len(res) - 1, -1, -1):
            for j in range(len(res[0])):
                if res[i][j] == "*":
                    output[i][j] = "*"
                elif res[i][j] > 0:
                    k = i
                    for _ in range(res[i][j]):
                        if k >= 0 and output[k][j] != "*":
                            output[k][j] = "#"
                            k -= 1

        return output