class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        def getMin(i, j):
            curMin = i
            for i in range(i, j - 1):
                if costs[i] < curMin:
                    curMin = i
            return curMin
        
        cost = 0
        for _ in range(k):
            num1 = getMin(0, candidates)
            num2 = getMin(len(costs) - candidates, len(costs))
            if costs[num1] <= costs[num2]:
                cost += costs[num1]
                costs.pop(num1)
            else:
                cost += costs[num2]
                costs.pop(num2)

        return cost