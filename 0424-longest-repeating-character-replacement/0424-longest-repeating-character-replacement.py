class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def check(count, k):
            first = 1
            for key in count:
                if first:
                    first = 0
                    continue
                if count[key] > k: return False
                k -= count[key]
            return True

        count = defaultdict(int)
        left, res = 0, 0
        for right in range(len(s)):
            count[s[right]] += 1
            while not check(count, k):
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            res = max(res, right - left + 1)
        return res
