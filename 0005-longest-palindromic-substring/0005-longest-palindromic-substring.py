class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        for i in range(len(s)):
            if i > 0 and s[i-1] == s[i]:
                left, right = self.checkPalindrome(s, i-1, i)
                if right - left + 1 > len(res):
                    res = s[left:right+1]
            if i < len(s) - 1 and s[i+1] == s[i]:
                left, right = self.checkPalindrome(s, i, i+1)
                if right - left + 1 > len(res):
                    res = s[left:right+1]
            if i > 0 and i < len(s) - 1:
                left, right = self.checkPalindrome(s, i-1, i+1)
                if right - left + 1 > len(res):
                    res = s[left:right+1]
        return res
        
    def checkPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1