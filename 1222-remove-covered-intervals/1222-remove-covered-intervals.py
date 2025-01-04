class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = [intervals[0]]

        for curStart, curEnd in intervals[1:]:
            prevStart, prevEnd = stack[-1]
            if prevStart == curStart and prevEnd <= curEnd:
                stack.pop()
            elif prevStart < curStart and prevEnd >= curEnd:
                continue
            stack.append([curStart, curEnd])
        
        return len(stack)