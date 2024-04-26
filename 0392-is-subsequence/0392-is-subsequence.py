class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        
        count = j = 0
        for i in range(len(t)):
            if s[j] == t[i]:
                count += 1
                j += 1
            
            if count == len(s):
                return True

        return False