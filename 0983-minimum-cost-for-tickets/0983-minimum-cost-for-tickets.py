class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        validDays = [False for _ in range(365+1)]
        memo = {}

        for n in days:
            validDays[n] = True
        
        def dfs(i):
            if i > 365:
                return 0
            if i in memo:
                return memo[i]
            
            if not validDays[i]:
                return dfs(i+1)

            oneDay =  costs[0] + dfs(i+1)
            sevenDay = costs[1] + dfs(i+7)
            thirtyDay = costs[2] + dfs(i+30)

            memo[i] = min(oneDay, sevenDay, thirtyDay) 
            return memo[i]
        
        return dfs(0)