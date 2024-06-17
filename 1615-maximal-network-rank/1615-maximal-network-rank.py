class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                curMax = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    curMax -= 1

                res = max(res, curMax)
        return res