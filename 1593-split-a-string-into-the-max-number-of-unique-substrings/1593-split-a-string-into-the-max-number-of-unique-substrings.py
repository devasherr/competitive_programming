class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def backtrack(start, visit):
            if start == n:
                return 0
            
            res = 0
            for end in range(start+1, n+1):
                cur = s[start:end]
                if cur not in visit:
                    visit.add(cur)
                    res = max(res, 1 + backtrack(end, visit))
                    visit.remove(cur)
            return res

        visit = set()
        return backtrack(0, visit)