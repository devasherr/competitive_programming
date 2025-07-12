class Solution:
    def twoCitySchedCost(self, costs) -> int:
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)
        n = len(costs)
        a, b = 0, 0
        res = 0

        for x, y in costs:
            if x < y:
                if a < n // 2:
                    res += x
                    a += 1
                else:
                    res += y
                    b += 1
            else:
                if b < n // 2:
                    res += y
                    b += 1
                else:
                    res += x
                    a += 1

        return res