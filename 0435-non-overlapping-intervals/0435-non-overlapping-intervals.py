class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res, curMax = 0, float("-inf")

        for i in range(len(intervals)):
            start, end = intervals[i]
            if start >= curMax:
                curMax = max(curMax, end)
                continue
            
            if end < curMax:
                curMax = end
            res += 1
            
        return res