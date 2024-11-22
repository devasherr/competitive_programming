class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        patterns = defaultdict(int)

        for i in range(rows):
            cur = []
            prev = matrix[i][0]

            for j in range(cols):
                if matrix[i][j] != prev:
                    cur.append("|")
                    prev = matrix[i][j]
                cur.append("_")
            
            patterns["".join(cur)] += 1
        
        res = 0
        for key in patterns:
            res = max(res, patterns[key])
        return res