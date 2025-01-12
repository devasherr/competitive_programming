class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        free, openCount = 0, 0
        for i in range(len(s)):
            if locked[i] == "0":
                free += 1
            else:
                if s[i] == ")":
                    if openCount > 0:
                        openCount -= 1
                    elif free > 0:
                        free -= 1
                    else:
                        return False
                else:
                    openCount += 1
        temp = openCount
        openCount -= free
        free -= temp
        
        if openCount > 0: return False
        return free % 2 == 0