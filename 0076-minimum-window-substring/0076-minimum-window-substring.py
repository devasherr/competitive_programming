class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(sCount, tCount):
            for key in tCount:
                if sCount[key] < tCount[key]:
                    return False
            return True

        sCount, tCount = defaultdict(int), Counter(t)
        left = 0
        res, resLength = "", float("inf")
        for right in range(len(s)):
            sCount[s[right]] += 1
            while check(sCount, tCount):
                if right - left + 1 < resLength:
                    res = s[left:right+1]
                    resLength = right - left + 1

                sCount[s[left]] -= 1
                left += 1

        return res
