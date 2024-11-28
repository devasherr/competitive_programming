class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        sMap, tMap = defaultdict(int), defaultdict(int)
        jump = len(s) // k
        
        for i in range(0, len(s) - jump + 1, jump):
            sMap[s[i:i+jump]] += 1
            tMap[t[i:i+jump]] += 1

        return sMap == tMap