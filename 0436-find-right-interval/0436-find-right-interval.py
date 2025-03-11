class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [n for n, _ in intervals]
        indexMap = {}
        for i in range(len(intervals)):
            indexMap[intervals[i][0]] = i
        
        intervals.sort()
        numsMap = {}

        def binarySearch(left, target):
            cur, right = float("inf"), len(intervals) - 1

            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] >= target:
                    cur = intervals[mid][0]
                    right = mid - 1
                else:
                    left = mid + 1
                
            return cur

        for i in range(len(intervals)):
            numsMap[intervals[i][0]] = binarySearch(i, intervals[i][1])
        
        for i in range(len(res)):
            if numsMap[res[i]] == float("inf"):
                res[i] = -1
                continue
            
            res[i] = indexMap[numsMap[res[i]]]
        
        return res