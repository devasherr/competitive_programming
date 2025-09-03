class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left, res = 0, 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]] == 2:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
