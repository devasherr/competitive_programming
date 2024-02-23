class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = [[0] * len(strs) for _ in range(len(strs[0]))]

        for i in range(len(strs)):
            for j in range(len(strs[0])):
                res[j][i] = strs[i][j]
        
        count = 0

        for r in res:
            if r != sorted(r):
                count += 1
        return count