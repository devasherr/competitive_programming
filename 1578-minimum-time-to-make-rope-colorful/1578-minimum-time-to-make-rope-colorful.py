class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        res, i = 0, 1
        while i < len(colors):
            cur, total= neededTime[i-1], neededTime[i-1]
            found = False
            if colors[i] == colors[i-1]: found = True

            while i < len(colors) and colors[i] == colors[i-1]:
                cur = max(cur, neededTime[i])
                total += neededTime[i]
                i += 1

            if found:
                res += total - cur

            i += 1

        return res
