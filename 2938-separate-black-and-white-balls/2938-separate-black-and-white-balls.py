class Solution:
    def minimumSteps(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        last = len(dp)-1 

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0": continue
            dp[i] = dp[last]
            dp[i] += last - i - 1

            last = i
        return sum(dp)