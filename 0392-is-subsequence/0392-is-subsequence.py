class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        removed = 0

        for i in range(len(t)):
            if t[i] == s[idx]:
                removed += 1
                idx += 1

                if removed == len(s):
                    return True

        return False