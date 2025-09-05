class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = [0] * 26, [0] * 26
        for c in s1:
            s1Count[ord(c) - ord("a")] += 1

        left = 0
        for right in range(len(s2)):
            s2Count[ord(s2[right]) - ord("a")] += 1
            if right - left + 1 < len(s1): continue

            if s1Count == s2Count:
                return True 
            s2Count[ord(s2[left]) - ord("a")] -= 1
            left += 1

        return False
