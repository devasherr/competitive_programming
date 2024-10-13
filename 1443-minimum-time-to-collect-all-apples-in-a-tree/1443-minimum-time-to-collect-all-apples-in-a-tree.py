class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(i, parent):
            time = 0

            for child in graph[i]:
                if child == parent:
                    continue 
                childTime = dfs(child, i)
                if childTime > 0 or hasApple[child]:
                    time += (childTime + 2)
            return time

        return dfs(0, -1)        