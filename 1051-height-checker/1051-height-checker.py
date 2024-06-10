class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        countSort = [0 for i in range(max(heights)+1)]

        # populate the count sort
        for h in heights:
            countSort[h] += 1
        
        expected = []
        for i in range(1, len(countSort)):
            for _ in range(countSort[i]):
                expected.append(i)
        
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        
        return res