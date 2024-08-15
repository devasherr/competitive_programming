class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dfs(i):
            if i >= len(questions): return 0
            if i in memo: return memo[i]
            
            memo[i] = max(questions[i][0] + dfs(i+questions[i][1]+1), dfs(i+1))
            return memo[i]

        memo = {}
        return dfs(0)