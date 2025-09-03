class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0 for _ in range(26)]
        left, res = 0, 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            while (right - left + 1) - max(count) > k:
                count[ord(s[left])- ord('A')] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res