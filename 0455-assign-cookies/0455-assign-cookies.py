class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # O(nlogn)
        g = sorted(g)
        s = sorted(s)

        i , count = 0, 0

        while i < len(s) and count < len(g):
            if s[i] >= g[count]:
                count += 1
            i += 1

        return count