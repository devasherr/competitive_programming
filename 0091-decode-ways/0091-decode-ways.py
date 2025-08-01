class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i):
            if i >= len(s):
                return 1
            if s[i] == "0": return 0
            if i in memo: return memo[i]

            one = dp(i+1)
            two = 0
            if i+2 <= len(s) and s[i:i+2] <= "26":
                two = dp(i+2)

            memo[i] = one + two
            return memo[i]
        
        memo = {}
        return dp(0)
