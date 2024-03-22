class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charCount = defaultdict(int)
        res = 0


        for right in range(len(s)):
            charCount[s[right]] += 1
            while charCount[s[right]] > 1:
                charCount[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res