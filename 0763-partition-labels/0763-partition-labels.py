class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexMap = {}
        for i in range(len(s) -1, -1, -1):
            if s[i] not in lastIndexMap:
                lastIndexMap[s[i]] = i
        
        res = []
        count = 0
        endIndex = 1

        for i in range(len(s)):
            count += 1
            if i == endIndex:
                res.append(count)
                count = 0
                continue
            
            if lastIndexMap[s[i]] > endIndex:
                endIndex = lastIndexMap[s[i]] 

        return res