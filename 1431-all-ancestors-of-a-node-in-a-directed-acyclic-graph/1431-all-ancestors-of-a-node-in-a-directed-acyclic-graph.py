class Solution:
    def getAncestors(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        visit = set()
        res = [[] for _ in range(n)]

        def dfs(node):
            if node in visit: return res[node]
            visit.add(node)
            if graph[node] == []: return []

            cur = []

            for child in graph[node]:
                cur.extend([child] + dfs(child))

            res[node] = sorted(set(cur))
            return cur

        for i in range(n):
            if i not in visit:
                dfs(i)
        
        return res