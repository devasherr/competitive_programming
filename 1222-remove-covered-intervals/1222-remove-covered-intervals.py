class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # cool sorting right :)
        intervals.sort(key = lambda x: (x[0], -1 * x[1]))
        stack = [intervals[0]]

        for curStart, curEnd in intervals[1:]:
            prevStart, prevEnd = stack[-1]
            if prevStart <= curStart and prevEnd >= curEnd:
                continue
            stack.append([curStart, curEnd])

        return len(stack)