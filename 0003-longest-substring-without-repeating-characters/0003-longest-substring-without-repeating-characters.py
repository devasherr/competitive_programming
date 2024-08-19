class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curCount = defaultdict(int)
        res, left = 0, 0

        for right in range(len(s)):
            curCount[s[right]] += 1
            while curCount[s[right]] > 1:
                curCount[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res