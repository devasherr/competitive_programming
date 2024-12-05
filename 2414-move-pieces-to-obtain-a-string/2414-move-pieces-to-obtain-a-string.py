class Solution:
    def canChange(self, start: str, target: str) -> bool:
        startList, targetList = [], []
        for i in range(len(start)):
            if start[i] != "_":
                startList.append((start[i], i))
            if target[i] != "_":
                targetList.append((target[i], i))
        
        if len(startList) != len(targetList): return False
        
        for i in range(len(startList)):
            if startList[i][0] != targetList[i][0]:
                return False
            if startList[i][0] == "L" and startList[i][1] < targetList[i][1]:
                return False
            if startList[i][0] == "R" and startList[i][1] > targetList[i][1]:
                return False
        return True