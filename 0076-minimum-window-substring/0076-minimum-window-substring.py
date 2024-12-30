class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = s + "a"
        left = 0

        sCount, tCount = defaultdict(int), Counter(t)
        for right in range(len(s)):
            sCount[s[right]] += 1
            while self.checkGood(tCount, sCount):
                if right - left + 1 < len(res):
                    res = s[left:right+1]

                sCount[s[left]] -= 1
                left += 1
                
        return res if len(res) < len(s) + 1 else ""

    def checkGood(self, tCount, sCount):
        for key in tCount:
            if sCount[key] < tCount[key]:
                return False
        return True