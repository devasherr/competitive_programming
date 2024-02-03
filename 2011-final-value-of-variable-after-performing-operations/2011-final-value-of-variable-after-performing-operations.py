class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        opeMap = {"X++" : 1, "++X" : 1, "--X" : -1, "X--": -1}
        
        x = 0
        for p in operations:
            x += opeMap[p]

        return x
