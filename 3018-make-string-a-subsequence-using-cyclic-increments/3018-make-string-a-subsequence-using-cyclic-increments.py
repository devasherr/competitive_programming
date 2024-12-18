class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            next_c = "a" if str1[i] == "z" else chr(ord(str1[i])+1)

            if str1[i] == str2[j] or next_c == str2[j]:
                j += 1
            i += 1
        return j >= len(str2)