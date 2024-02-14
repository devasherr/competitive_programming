class Solution:
    def reverseWords(self, s: str) -> str:
        res = list(s.split())
        return " ".join(res[::-1])