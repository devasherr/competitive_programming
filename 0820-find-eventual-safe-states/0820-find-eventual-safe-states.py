class Solution:
    def eventualSafeNodes(self, graph):
        visit = set()
        def dfs(node):
            if node in visit: return False
            if graph[node] == []: return True
            visit.add(node)

            good = True
            for child in graph[node]:
                if not dfs(child):
                    good = False
            
            if not good: return False

            graph[node] = []
            visit.remove(node)
            return True
        
        for i in range(len(graph)):
            dfs(i)
        
        res = []
        for i in range(len(graph)):
            if graph[i] == []:
                res.append(i)
        return res
