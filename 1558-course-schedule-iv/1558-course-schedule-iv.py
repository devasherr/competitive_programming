class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(cur, target, visit):
            if cur == target: return True
            if cur in visit: return False
            
            visit.add(cur)
            val = False
            for child in graph[cur]:
                val |= dfs(child, target, visit)
            return val

        res = []
        for u, v in queries:
            res.append(dfs(u, v, set()))
        
        return res