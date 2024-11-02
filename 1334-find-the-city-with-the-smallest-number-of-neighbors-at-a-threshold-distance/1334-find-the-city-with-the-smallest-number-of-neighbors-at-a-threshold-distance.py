class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        n = len(edges)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i, j, w in edges:
            dp[i][j] = w
            dp[j][i] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        count = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if dp[i][j] <= distanceThreshold:
                    count[i] += 1
                    
        res, bound = n, float("inf")
        for key, value in count.items():
            if value < bound:
                res = key
                bound = value
            elif value == bound:
                res = max(res, key)
        
        return res