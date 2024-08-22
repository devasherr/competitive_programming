class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        mLen=1
        mStr=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > mLen and s[i:j+1] == s[i:j+1][::-1]:
                    mLen = j-i+1
                    mStr = s[i:j+1]

        return mStr
        