class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dfs(i, cost):
            if i >= len(questions):
                return cost

            if (i, cost) not in cache:
                cache[(i, cost)] = max(dfs(i+questions[i][1]+1, cost+questions[i][0]), dfs(i+1, cost))

            return cache[(i, cost)]
        
        cache = {}
        return dfs(0, 0)