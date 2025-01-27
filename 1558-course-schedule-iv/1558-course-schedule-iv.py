class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        preSet = defaultdict(set)
        def dfs(node):
            if preSet[node]: return preSet[node]
            vals = set()
            for child in graph[node]:
                vals = vals.union(dfs(child))
                vals.add(child)
            
            for v in vals:
                preSet[node].add(v)
            return preSet[node]
        
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for u, v in queries:
            ans = True if v in preSet[u] else False
            res.append(ans)
        return res