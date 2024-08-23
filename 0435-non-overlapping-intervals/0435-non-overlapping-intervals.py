class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        print(intervals)
        res = 0
        for interval in intervals[1:]:
            if interval[0] < end:
                end = min(end, interval[1])
                res += 1
                continue
            start, end = interval[0], interval[1]

        return res