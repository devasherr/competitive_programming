class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newTime = []
        for interval in intervals:
            if not newInterval:
                newTime.append(interval)
                continue

            if interval[0] <= newInterval[0]:
                newTime.append(interval)
            else:
                newTime.append(newInterval)
                newTime.append(interval)
                newInterval = []
        if newInterval: newTime.append(newInterval)
        
        res = []
        for interval in newTime:
            if not res:
                res.append(interval)
                continue
            
            if interval[0] <= res[-1][1]:
                cur = res.pop()
                first = min(cur[0], interval[0])
                last = max(cur[1], interval[1])

                res.append([first, last])
            else:
                res.append(interval)
            
        return res