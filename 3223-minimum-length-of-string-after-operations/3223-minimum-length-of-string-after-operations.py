class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        res = 0

        for key in count:
            if count[key] % 2 == 0:
                res += 2
            else:
                res += 1
        return res