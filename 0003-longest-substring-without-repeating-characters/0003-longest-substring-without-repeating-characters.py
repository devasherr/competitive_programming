class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = []
        maxLength = 0
        while l < len(s):
            if s[l] in res:
                res.pop(0)
                continue

            res.append(s[l])
            maxLength = max(maxLength, len(res))
            l += 1
        
        return maxLength