class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid)):
                count[grid[i][j]] += 1
        
        for i in range(1, len(grid) ** 2 + 1):
            if count[i] == 2:
                d = i
            if count[i] == 0:
                m = i

        return [d, m]